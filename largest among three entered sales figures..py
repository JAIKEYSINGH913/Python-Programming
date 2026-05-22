# 7
# Write a program to find the largest among three entered sales figures.

sales1 = int(input("Enter first sales figure: "))
sales2 = int(input("Enter second sales figure: "))
sales3 = int(input("Enter third sales figure: "))

# Find the largest figure
if sales1 >= sales2 and sales1 >= sales3:
    largest = sales1
elif sales2 >= sales1 and sales2 >= sales3:
    largest = sales2
else:
    largest = sales3

print("The largest sales figure is:", largest)
