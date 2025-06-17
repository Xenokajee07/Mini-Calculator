# profit_tracker.py

def show_menu():
    print("\n=== Profit Tracker ===")
    print("1. Add Profit")
    print("2. View Profits")
    print("3. View Total Earnt")
    print("4. Thank You Nisa")

# Dictionary to store profits
profits = {}

# Start infinite menu loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter profit name (e.g. FMCG): ")
        amount = float(input("Enter amount earned: "))
        profits[name] = profits.get(name, 0) + amount
        print(f"{name} recorded with R{amount:.2f}")

    elif choice == "2":
        if not profits:
            print("No profits yet.")
        else:
            print("\n--- All Profits ---")
            for name, amount in profits.items():
                print(f"{name}: R{amount:.2f}")

    elif choice == "3":
        total = sum(profits.values())
        print(f"Total earned: R{total:.2f}")

    elif choice == "4":
        print("Thank You Nisa!")
        break

    else:
        print("Invalid option. Try again.")

