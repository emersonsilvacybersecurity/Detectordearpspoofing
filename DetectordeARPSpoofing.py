import scapy.all as scapy
import sys
import time

class ArpShield:
    def __init__(self):
        print("\n" + "="*60)
        print("DETECTOR DE ARP SPOOFING - MONITOR SOC (WINDOWS READY)")
        print("="*60)
        
        # IP do seu roteador (visto no seu terminal)
        self.gateway_ip = "192.168.15.1"
        
        # Travamos o MAC manualmente para evitar o bloqueio do Windows
        self.real_mac = "84:d8:bb:83:59:78" 
        
        print(f"[*] Gateway Protegido: {self.gateway_ip}")
        print(f"[*] MAC de Confiança: {self.real_mac}")
        print("[+] Monitoramento ativo... (Ctrl+C para encerrar)")
        print("-" * 60)

    def process_packet(self, packet):
        """Analisa pacotes ARP e detecta anomalias."""
        if packet.haslayer(scapy.ARP):
            # Se o IP de origem for o do nosso Gateway
            if packet[scapy.ARP].psrc == self.gateway_ip:
                # Normalizamos os MACs para comparação
                claimed_mac = packet[scapy.ARP].hwsrc.lower().replace("-", ":")
                trusted_mac = self.real_mac.lower().replace("-", ":")
                
                # Se o MAC que chegou for diferente do MAC legítimo: ALERTA!
                if trusted_mac != claimed_mac:
                    self.trigger_alert(packet[scapy.ARP].psrc, claimed_mac, self.real_mac)

    def trigger_alert(self, ip, attacker_mac, original_mac):
        """Gera o Alerta Técnico conforme MITRE T1557.002."""
        print("\n" + "!"*60)
        print(f" [ALERTA] - INCIDENTE DETECTADO ÀS {time.strftime('%H:%M:%S')}")
        print(f"TÉCNICA MITRE: ARP Cache Poisoning (T1557.002)")
        print(f"ALVO: {ip}")
        print(f"MAC REAL (Legítimo): {original_mac}")
        print(f"MAC FALSO (Atacante): {attacker_mac}")
        print("-" * 60)
        print("AÇÃO SUGERIDA: Isolar o dispositivo atacante na rede.")
        print("!"*60 + "\n")

    def start(self):
        try:
            # Captura pacotes sem filtro para garantir a detecção no Windows
            scapy.sniff(store=False, prn=self.process_packet)
        except KeyboardInterrupt:
            print("\n[*] Monitoramento encerrado."); sys.exit(0)

if __name__ == "__main__":
    shield = ArpShield()
    shield.start()