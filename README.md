# Personal Expense Tracker

## Project Description
The Personal Expense Tracker is a Python command-line application that helps users record, view, filter, and analyze their daily expenses. It stores expense data in a CSV file so that records remain saved even after the program is closed.

## Features
- Add new expenses with date, category, description, and amount.
- View all recorded expenses in a formatted table.
- Filter expenses by category or month.
- Calculate total expenses for each category.
- Display the grand total of all expenses.
- Identify the biggest single expense.
- Validate dates, amounts, and user input.
- Store expenses in a CSV file for persistent storage.

## Technologies Used
- Python
- CSV module
- VS Code

## Project Structure

```text
project03_expense_tracker/
├── main.py
├── expenses.csv
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
py main.py
```

## Menu Options

1. Add Expense
2. View All Expenses
3. Filter Expenses
4. Expense Summary
5. Exit

## CSV Data Format

Expenses are stored in `expenses.csv` with the following columns:

- `date` — Expense date in YYYY-MM-DD format.
- `category` — Expense category.
- `description` — Details of the expense.
- `amount` — Expense amount.

## Testing
- Added and displayed 10 sample expense records.
- Tested filtering by category and month.
- Verified category totals and the grand total.
- Checked the biggest expense.
- Restarted the application and confirmed that saved expenses persisted.

## Problem Fixed
The application was extended beyond basic expense entry to support viewing, filtering, category summaries, and input validation. CSV persistence was tested by restarting the program and confirming that all saved records remained available.

## Note
The included expenses are fictional sample data for testing and demonstration purposes.
