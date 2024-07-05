from portscanner.portscanner import PortScanner

scanner = PortScanner("192.168.1.1", 200, 202) # update the values
open_ports = scanner.scan_ports()
print("Open ports: ", open_ports)