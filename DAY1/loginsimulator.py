# Predefined username and password
correct_username = "jyothi"
correct_password = "1234"

# User input
username = input("Enter username: ")
password = input("Enter password: ")
# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful!")
    
    
else:    print("Login failed! Incorrect username or password.")