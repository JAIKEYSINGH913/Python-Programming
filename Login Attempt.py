# Q9
# Create a login attempt system that allows the user a maximum of 3 attempts using a while loop.

correct_password = "secure123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Enter your password: ")
    attempts += 1

    if guess == correct_password:
        print("Login successful! Welcome back.")
        break
    else:
        remaining = max_attempts - attempts
        print(f"Incorrect password. Attempts remaining: {remaining}")

if attempts == max_attempts and guess != correct_password:
    print("Account locked. Too many attempts.")
