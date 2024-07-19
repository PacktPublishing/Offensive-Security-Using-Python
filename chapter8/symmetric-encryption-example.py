from cryptography.fernet import Fernet 


# Generate a key 
key = Fernet.generate_key() 
cipher_suite = Fernet(key) 

# Encrypt a message 
cipher_text = cipher_suite.encrypt(b"Secret message") 
print(f"Cipher Text: {cipher_text}") 

# Decrypt the message 
plain_text = cipher_suite.decrypt(cipher_text) 
print(f"Plain Text: {plain_text.decode()}") 