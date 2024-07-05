# Creating a Simple TCP Client
import socket
target_host = "example.com"
target_port = 80
# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect((target_host, target_port))
# Send data
client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
# Receive data
response = client.recv(4096)
# Print the response
print(response)