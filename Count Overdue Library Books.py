# Q12
# A library system wants to count how many overdue books exist in a list of borrowed books.

borrowed_books = [
    {"title": "Python ", "is_overdue": True},
    {"title": "Data Science", "is_overdue": False},
    {"title": "The Hobbit", "is_overdue": True},
    {"title": "Bio 10", "is_overdue": False}
]

overdue_count = 0

for book in borrowed_books:
    if book["is_overdue"] == True:
        overdue_count += 1

print(f"Total number of overdue books: {overdue_count}")

