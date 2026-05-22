# Q21
# A bookstore wants to search whether a particular book exists in the inventory list.

inventory = ["The Hobbit", "2001", "To Kill a Mockingbird", "blood book"]
search_book = input("Enter book title to search: ")

found = False
for book in inventory:
    if book.lower() == search_book.lower():
        found = True
        break

if found:
    print("Yes, the book is available in our inventory!")
else:
    print("Sorry, this book is out of stock.")
