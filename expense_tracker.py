# expense_tracker.py

def show_menu():
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")

# Dictionary to store expenses
expenses = {}

# Start infinite menu loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter expense name (e.g. Groceries): ")
        amount = float(input("Enter amount spent: "))
        expenses[name] = expenses.get(name, 0) + amount
        print(f"{name} recorded with R{amount:.2f}")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\n--- All Expenses ---")
            for name, amount in expenses.items():
                print(f"{name}: R{amount:.2f}")

    elif choice == "3":
        total = sum(expenses.values())
        print(f"Total spent: R{total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

