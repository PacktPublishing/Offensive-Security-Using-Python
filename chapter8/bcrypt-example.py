import bcrypt 

def hash_password(password): 
    salt = bcrypt.gensalt() 
    return bcrypt.hashpw(password.encode(), salt) 


def check_password(password, hashed): 
    return bcrypt.checkpw(password.encode(), hashed) 

# Example usage: 
password = "securepassword" 
hashed_password = hash_password(password) 
print(f"Hashed Password: {hashed_password}") 

# Verify the password 
is_valid = check_password("securepassword", hashed_password) 
print(f"Password is valid: {is_valid}") 