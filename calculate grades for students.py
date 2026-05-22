# 8
# A school wants to calculate grades for students based on marks obtained in five subjects.

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(mark)

totalmarks = sum(marks)
average = totalmarks / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'


print(f"Total Marks: {totalmarks} / 500")
print(f"Average Percentage: {average:.2f}%")
print(f"Grade: {grade}")
