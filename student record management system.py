# Q20
# Create a student record management system using dictionaries.

student_records = {
    "S01": {"name": "Alice", "age": 20, "marks": "A"},
    "S02": {"name": "Bob", "age": 21, "marks": "B"}
}

search_id = input("Enter Student ID to view details (e.g., S01): ")

if search_id in student_records:
    student = student_records[search_id]
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"marks: {student['grade']}")
else:
    print("Student record not found.")
