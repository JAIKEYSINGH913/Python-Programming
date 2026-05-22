# 2
# A company wants to identify whether an employee is eligible for a bonus
#based on attendance percentage and performance rating.

# Get employee details
name = input("Enter employee name: ")
attendance = float(input("Enter attendance percentage (e.g., 95): "))
rating = float(input("Enter performance rating (1 to 5): "))

# Check if they meet both requirements
if attendance >= 90 and rating >= 4:
    print(name, "is ELIGIBLE for a bonus!")
else:
    print(name, "is NOT eligible for a bonus.")
