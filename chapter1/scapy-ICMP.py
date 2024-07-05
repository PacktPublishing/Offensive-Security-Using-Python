# Creating a Basic ICMP Ping Packet
# Import the IP,ICMP and sr1 from Scapy module
from scapy.all import IP, ICMP, sr1

# Create an ICMP packet
packet = IP(dst="192.168.1.1") / ICMP()

# Send the packet and receive a response
response = sr1(packet)
