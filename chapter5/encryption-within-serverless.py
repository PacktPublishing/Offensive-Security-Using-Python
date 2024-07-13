from cryptography.fernet import Fernet
# Encrypt data in a Lambda function using Fernet encryption
def encrypt_data(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data