# Import the necessary modules from Scapy
from scapy.all import ARP, Ether, srp

# Function to perform ARP scan
def arp_scan(target_ip):
    # Create an ARP request packet
    arp_request = ARP(pdst=target_ip)
    # Create an Ethernet frame to encapsulate the ARP request
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff") #Broadcasting to all devices in the network

    # Combine the Ethernet frame and ARP request packet
    arp_request_packet = ether_frame / arp_request

    # Send the packet and receive the response
    result = srp(arp_request_packet, timeout=3, verbose=False)[0]
    # List to store the discovered devices
    devices_list = []

    # Parse the response and extract IP and MAC addresses
    for sent, received in result: 
        devices_list.append({'ip': received.psrc,'mac': received.hwsrc})

    return devices_list

# Function to print scan results
def print_scan_results(devices_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices_list:
        print(f"{device['ip']}\t\t{device['mac']}")

# Main function to perform the scan
def main(target_ip):
    print(f"Scanning {target_ip}...")
    devices_list = arp_scan(target_ip)
    print_scan_results(devices_list)

# Entry point of the script
if __name__ == "__main__":
    # Define the target IP range (e.g.,"192.168.1.1/24")
    target_ip = input("Enter the target IP range (e.g.,92.168.1.1/24): ")
    main(target_ip)