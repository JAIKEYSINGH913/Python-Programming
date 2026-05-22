# Question 1
# A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount.
# Write a program using if...elif...else to display the final amount.

# Input the total purchase amount
purchasing_amount = float(input("Enter the total purchase amount: "))

# Step 2: Determine discount percentage using if...elif...else
if purchasing_amount >= 1000:
    discount_percent = 20  # 20% discount for amounts 1000 and above
elif purchasing_amount >= 500:
    discount_percent = 10  # 10% discount for amounts between 500 and 999
elif purchasing_amount >= 100:
    discount_percent = 5   # 5% discount for amounts between 100 and 499
else:
    discount_percent = 0   # No discount for amounts below 100

# discount and final amount
discount_amount = (discount_percent / 100) * purchasing_amount
final_amount = purchasing_amount - discount_amount

# print the final bill details
print(f"Original Amount: RS{purchasing_amount:.2f}")
print(f"Discount Applied: {discount_percent}% ( RS{discount_amount:.2f})")
print(f"Final Amount to Pay: RS {final_amount:.2f}")

