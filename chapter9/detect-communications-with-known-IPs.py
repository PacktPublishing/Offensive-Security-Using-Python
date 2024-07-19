from scapy.all import sniff, IP

def analyze_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        # Example: Detecting communication with known malicious IP
        if ip_dst in malicious_ips:
            print(f"Suspicious communication detected:{ip_src} -> {ip_dst}")
            
malicious_ips = ['192.168.1.1', '10.0.0.1']
sniff(filter="ip", prn=analyze_packet)