from datetime import datetime

def add_expense():
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of expense (e.g., Food, Transport, Entertainment): ").strip().title()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("expenses.csv", "a") as file:
        file.write(f"{timestamp}, {amount}, {category}\n")

    print("\nExpense Added Successfully!\n")
    print(f"Amount: ₹{amount:.2f}")
    print(f"Category: {category}")

def view_expenses():
    print("\nAll Expenses:\n")
    with open("expenses.csv", "r") as file:
        for line in file:
            timestamp, amount, category = line.strip().split(",")
            print("-"*20)
            print(f"Date: {timestamp}\nAmount: ₹{float(amount):.2f}\nCategory: {category}")
            print("-"*20)


def view_total():
    total = 0
    with open("expenses.csv", "r") as file:
        for line in file:
            timestamp, amount, category = line.strip().split(",")
            total += float(amount)

    print(f"\nTotal Expenses: ₹{total:.2f}")

def delete_all_expenses():
    choice1 = input("Enter 'y'-> yes OR 'n'->no and go back to menu:")
    if choice1.lower() == "y":
        with open("expenses.csv", "w") as file:
            file.write("")
        print("\nAll expenses deleted successfully!")
    elif choice1.lower() == "n":
        print("\nDeletion Cancelled")
    else:
        print("\nInvalid input")

def search_by_category():
    search_category = input("Enter Category: ")
    print(f"Expenses in {search_category}")
    with open("expenses.csv","r") as file:
        found = False
        total = 0
        for line in file:
            amount, category = line.strip().split(",")
            if category.lower() == search_category.lower():
                print(f"Amount: ₹{amount}\n")
                found = True
                total+= float(amount)
        if not found:
            print(f"\n No expenses found in {search_category} category.")
        else:
            print(f"\nTotal Expenses in {search_category}: ₹{total:.2f}")

def category_summary():
	category_totals = {}
	with open("expenses.csv","r") as file:
		for line in file:
			timestamp, amount, category = line.strip().split(",")
			if category in category_totals:
				category_totals[category] += float(amount)
			else:
				category_totals[category] = float(amount)
			
		for category, amount in category_totals.items():
			print(f"{category} : ₹{float(amount):.2f}\n")

while True:

    print("=" * 40)
    print("      Expense Tracker")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Search by Category")
    print("5. Delete all expenses")
    print("6. View category summary")
    print("7. Exit")
    

    choice = input("Enter your choice: ")
    if choice=="7":
        print("Thank you for using Expense Tracker!")
        break
    elif choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        view_total()
    elif choice=="4":
        search_by_category()
    elif choice=="5":
            delete_all_expenses()
    elif choice=="6":
        category_summary()
    else:
        print("Invalid choice. Please try again!.")

