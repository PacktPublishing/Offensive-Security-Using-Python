from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import hashes 

# Generate a private key 
private_key = rsa.generate_private_key( 
    public_exponent=65537, 
    key_size=2048,
) 

# Generate the corresponding public key 
public_key = private_key.public_key() 

# Serialize the private key 
pem = private_key.private_bytes( 
    encoding=serialization.Encoding.PEM, 
    format=serialization.PrivateFormat.TraditionalOpenSSL, 
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword') 

) 

# Serialize the public key 
public_pem = public_key.public_bytes( 
    encoding=serialization.Encoding.PEM, 
    format=serialization.PublicFormat.SubjectPublicKeyInfo 
)

# Encrypt a message using the public key 
message = b"Secret message" 
cipher_text = public_key.encrypt( 
    message, 
    padding.OAEP( 
        mgf=padding.MGF1(algorithm=hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None 
    ) 
) 
print(f"Cipher Text: {cipher_text}") 

# Decrypt the message using the private key 
plain_text = private_key.decrypt( 

    cipher_text, 
    padding.OAEP( 
        mgf=padding.MGF1(algorithm=hashes.SHA256()), 
        algorithm=hashes.SHA256(), 
        label=None 
    ) 
) 
print(f"Plain Text: {plain_text.decode()}") 