# Q10
# A food delivery app wants to display menu items repeatedly until the user selects Exit.


while True:
    print("\n--- Pizza Delivery Menu ---")
    print("1. Cheese Pizza")
    print("2. Pepperoni Pizza")
    print("3. Veggie Pizza")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print("Added Cheese Pizza to your cart!")
    elif choice == "2":
        print("Added Pepperoni Pizza to your cart!")
    elif choice == "3":
        print("Added Veggie Pizza to your cart!")
    elif choice == "4":
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
