import hashlib  

def hash_password(password): 
   return hashlib.sha256(password.encode()).hexdigest() 

# Example usage: 
password = "securepassword" 
hashed_password = hash_password(password) 
print(f"Hashed Password: {hashed_password}")