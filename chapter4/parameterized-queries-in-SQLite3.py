import sqlite3
username = input("Enter username: ")
password = input("Enter password: ")
# Establish a database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Use a parameterized query to prevent SQL injection
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

# Fetch the result
result = cursor.fetchone()

# Validate the login
if result:
    print("Login successful!")
else:
    print("Invalid credentials.")

# Close the connection
conn.close()