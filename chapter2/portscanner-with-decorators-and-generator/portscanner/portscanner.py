import socket
import time

#Class Definition
class PortScanner:
    def __init__(self, target_host, start_port,end_port):
        self.target_host = target_host
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
    #timing_decorator Decorator Method
    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Scanning took {end_time - start_time:.2f} seconds.")
            return result
        return wrapper
    #is_port_open Method
    def is_port_open(self, port):
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((self.target_host, port))
            return True
        except (socket.timeout,ConnectionRefusedError):
            return False
    #scan_ports Method
    @timing_decorator
    def scan_ports(self):
        open_ports = [port for port in range(self.start_port, self.end_port + 1) if self.is_port_open(port)]
        return open_ports
    #scan_ports_generator Method
    @timing_decorator
    def scan_ports_generator(self):
        for port in range(self.start_port,self.end_port + 1):
            if self.is_port_open(port):
                yield port

def main(): # type: ignore
    target_host = input("Enter target host: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    scanner = PortScanner(target_host, start_port,end_port)

    open_ports = scanner.scan_ports()
    print("Open ports: ", open_ports)

    open_ports_generator = scanner.scan_ports_generator()
    print("Open ports (using generator):", list(open_ports_generator))

if __name__ == "__main__":
    main()