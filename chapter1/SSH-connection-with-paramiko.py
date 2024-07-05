# SSH Connection with Paramiko
import paramiko
# Create an SSH client
ssh_client = paramiko.SSHClient()
# Automatically add the server's host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to the SSH server
ssh_client.connect("example.com", username="user",
password="password") # Update the credentials here

# Execute a command
stdin, stdout, stderr = ssh_client.exec_command("ls -l")

# Print the command output
print(stdout.read().decode("utf-8"))

# Close the SSH connection
ssh_client.close()
