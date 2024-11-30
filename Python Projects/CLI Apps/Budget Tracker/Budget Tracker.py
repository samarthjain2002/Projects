import argparse
import csv
from datetime import datetime
from tabulate import tabulate
import matplotlib.pyplot as plt


DATA_FILE = "budget_data.csv"

def add(amount, type, category, desc):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  amount, type, category, desc])
    print(f"Transaction added: {amount} {type} in {category} - {desc}")


def view():
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            transactions = [row for row in reader]
            if transactions:
                print(tabulate(transactions, headers = ["DATE & TIME", "AMOUNT", "TYPE", "CATEGORY", "DESCRIPTION"], tablefmt = "grid"))
            else:
                print("No transactions found.")
    except FileNotFoundError:
        print("No transactions found. Start by adding one.")


def summary():
    try:
        with open(DATA_FILE, mode = 'r') as file:
            reader = csv.reader(file)
            total_income = total_expenses = 0
            for row in reader:
                amount = float(row[1])
                if row[2] == "income":
                    total_income += amount
                else:
                    total_expenses += amount
            balance = total_income - total_expenses
            print(f"Total income: {total_income}")
            print(f"Total expenses: {total_expenses}")
            print(f"Balance: {balance}")
    except FileNotFoundError:
        print("No transactions found. Start by adding one.")


def visualize():
    try:
        with open(DATA_FILE, mode = 'r') as file:
            reader = csv.reader(file)
            category_totals = {}
            for row in reader:
                amount = float(row[1])
                if row[2] == "expense":
                    category_totals[row[3]] = category_totals.get(row[3], 0) + amount
            
            if category_totals:
                plt.figure(figsize = (8, 6))
                plt.pie(category_totals.values(), labels = category_totals.keys(), autopct = "%1.1f%%", startangle = 140)
                plt.title("Spending by category")
                plt.show()
            else:
                print("No expenses data found for visualization")
    except FileNotFoundError:
        print("o transactions found. Start by adding one.")


def main():
    parser = argparse.ArgumentParser(description = "Budget Tracker CLI")
    sub_parsers = parser.add_subparsers(dest = "command")

    add_parser = sub_parsers.add_parser("add", help = "Add a transaction")
    add_parser.add_argument("--amount", required=True, type = float, help = "Amount of transaction")
    add_parser.add_argument("--type", required=True, choices=["income", "expense"], help = "Type of transaction")
    add_parser.add_argument("--category", required=True, type = str, help = "Transaction category")
    add_parser.add_argument("--desc", required=True, type = str, help = "Description of the transaction")

    view_parser = sub_parsers.add_parser("view", help = "View the transactions")

    summary_parser = sub_parsers.add_parser("summarize", help = "Give summary of transactions")

    visualize_parser = sub_parsers.add_parser("visualize", help = "Visualize the transactions")

    args = parser.parse_args()

    if args.command == "add":
        add(args.amount, args.type, args.category, args.desc)
    elif args.command == "view":
        view()
    elif args.command == "summarize":
        summary()
    elif args.command == "visualize":
        visualize()


if __name__ == "__main__":
    main()