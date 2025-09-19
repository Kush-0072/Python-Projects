import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nAll Expenses:")
    for e in expenses:
        print(f"{e['date']} - {e['category']} - {e['amount']}")

def show_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    print("\nExpense Summary by Category:")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")

def main():
    expenses = load_expenses()
    while True:
        print("\nOptions: 1.Add Expense  2.View Expenses  3.Show Summary  4.Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Exiting. Have a nice day!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
