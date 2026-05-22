# 6
# A movie theatre wants to assign ticket pricing based on age categories such as child, adult, and senior citizen.

# age input user
age = int(input("Enter your age: "))

# price based on age
if age <= 12:
    print("Ticket Price: RS 10 (Child)")
elif age <= 64:
    print("Ticket Price: RS 15 (Adult)")
else:
    print("Ticket Price: RS 12 (Senior)")
