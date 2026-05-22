# Q16.
# A teacher wants to store marks of students in a list and display the average marks.

marks = [85, 92, 78, 90, 88]

total = 0
for m in marks:
    total += m

# Count elements manually or use len()
count = 0
for m in marks:
    count += 1

average = total / count
print(f"Marks List: {marks}")
print(f"Average Marks: {average}")
