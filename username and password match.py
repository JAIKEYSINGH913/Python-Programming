# 3
# Create a program to check whether a given username and password match predefined credentials.

# Predefined credentials
USERNAME = "JAIKEY SINGH"
PASSWORD = "1234567890"

# Get input from the user
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

# Verify and print the result

if user_input == USERNAME and pass_input == PASSWORD:
    print("Access Granted: Login successful!")
else:
    print("Access Denied: Incorrect username or password.")
