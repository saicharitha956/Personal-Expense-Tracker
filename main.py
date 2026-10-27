
import csv
import os
from datetime import date, datetime

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


# Load expenses from CSV
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# Add a new expense
def add_expense():
    print("\n=== Add Expense ===")

    expense_date = input(
        "Enter date (YYYY-MM-DD), or press Enter for today: "
    ).strip()

    if expense_date == "":
        expense_date = str(date.today())
    else:
        try:
            datetime.strptime(expense_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD.")
            return

    category = input("Enter category: ").strip().title()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()

        writer.writerow({
            "date": expense_date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}"
        })

    print("Expense saved successfully!")


# Display expenses in a table
def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nDate         Category       Description              Amount")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<14} "
            f"{expense['description']:<24} "
            f"{float(expense['amount']):>8.2f}"
        )


# View all expenses
def view_expenses():
    print("\n=== All Expenses ===")
    display_expenses(load_expenses())


# Filter expenses by category or month
def filter_expenses():
    expenses = load_expenses()

    print("\n=== Filter Expenses ===")
    print("1. Filter by category")
    print("2. Filter by month (YYYY-MM)")

    choice = input("Choose an option (1-2): ").strip()

    if choice == "1":
        category = input("Enter category: ").strip().casefold()
        filtered = [
            e for e in expenses
            if e["category"].casefold() == category
        ]

    elif choice == "2":
        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month format. Use YYYY-MM.")
            return

        filtered = [
            e for e in expenses
            if e["date"].startswith(month)
        ]

    else:
        print("Invalid choice.")
        return

    display_expenses(filtered)


# Category and overall summaries
def expense_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses available for summary.")
        return

    totals = {}
    grand_total = 0.0
    biggest_expense = expenses[0]

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        totals[category] = totals.get(category, 0.0) + amount
        grand_total += amount

        if amount > float(biggest_expense["amount"]):
            biggest_expense = expense

    print("\n=== Expense Summary ===")
    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")

    print(f"\nGrand total: {grand_total:.2f}")
    print(
        "Biggest expense:",
        biggest_expense["description"],
        f"({float(biggest_expense['amount']):.2f})"
    )


# Main menu
def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            expense_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
