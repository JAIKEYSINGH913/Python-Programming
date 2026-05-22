# 5
# A bank wants to calculate simple interest for customers based on principal, rate, and time entered by the user.

# user inputs
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the annual interest rate (in %): "))
time = int(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"\nThe simple interest is: {simple_interest:.2f}")
print(f"Total amount (Principal + Interest): {principal + simple_interest:.2f}")
