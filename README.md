# Mac-Spoofing

# 🎭 PoC: MAC Address Spoofing

![Status](https://img.shields.io/badge/Estado-Finalizado-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scapy](https://img.shields.io/badge/Library-Scapy-yellow)

## 📋 Descripción Técnica
Herramienta desarrollada en Python que automatiza el proceso de suplantación de identidad física (MAC Spoofing). El script interactúa con el sistema operativo para modificar la dirección de hardware de la interfaz de red y utiliza **Scapy** para inyectar tráfico ICMP inmediatamente, forzando a los switches de la red a actualizar sus tablas CAM (Content Addressable Memory) con la nueva identidad del atacante.

**Objetivo:** Demostrar cómo un atacante puede evadir controles de acceso básicos o listas blancas (Whitelisting) suplantando la dirección física de un dispositivo autorizado.

## 🗺️ Escenario de Prueba

| Dispositivo | Rol | Estado Inicial | Estado Final (Spoofed) |
| :--- | :--- | :--- | :--- |
| **Kali Linux** | Atacante | `Original:MAC` | `10:12:12:13:14:14` |
| **Switch IOU** | Víctima | Conoce la MAC real | Aprende la MAC falsa |

## 🚀 Uso
1.  **Permisos:** Root (sudo).
2.  **Ejecución:**
    ```bash
    sudo python3 mac_spoofing.py
    ```

## 📸 Evidencia
<img width="1755" height="658" alt="image" src="https://github.com/user-attachments/assets/ec792ffb-7e04-4aa5-b7c3-78329497a523" />


## 🛡️ Mitigación
* **Port Security:** Configurar `switchport port-security mac-address sticky`. Esto "memoriza" la primera MAC que se conecta y bloquea cualquier cambio posterior, impidiendo el spoofing.
* **Network Access Control (NAC):** Implementar 802.1X para autenticación basada en credenciales/certificados, no solo en MAC.

---
**Autor:** Cristopher De Los Santos  
**Matrícula:** 2024-1414
