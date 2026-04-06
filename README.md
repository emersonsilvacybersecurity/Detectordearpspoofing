#  ARP Shield - IDS de Detecção de ARP Spoofing (MITRE T1557.002)

Este projeto demonstra a detecção em tempo real de ataques de envenenamento de cache ARP (ARP Poisoning), simulando um cenário de **Adversary-in-the-Middle (AiTM)**.

##  Funcionalidades
- **Monitoramento Passivo:** Utiliza Sniffing de rede para validar pacotes ARP.
- **Detecção de Anomalias:** Compara o MAC do Gateway em tempo real com um banco de confiança.
- **Mapeamento MITRE:** Alertas estruturados com base na técnica T1557.002.

##  Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Biblioteca:** Scapy (Manipulação de pacotes de rede)
- **SO:** Windows/Linux (Requer privilégios de Administrador)


##  Aviso Legal (Disclaimer)
Este software foi desenvolvido para fins estritamente educacionais e laboratoriais como parte da minha graduação em Segurança Cibernética na UniCesumar. O uso destas ferramentas em redes de terceiros sem autorização explícita é ilegal e antiético.
