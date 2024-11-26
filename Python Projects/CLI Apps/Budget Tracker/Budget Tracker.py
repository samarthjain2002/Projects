import argparse
import csv
from datetime import datetime
from tabulate import tabulate


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
    except FileNotFoundError as e:
        print("No transactions found. Start by adding one.")


def summary():
    pass


def visualize():
    pass


def main():
    parser = argparse.ArgumentParser(description = "Budget Tracker CLI")
    sub_parsers = parser.add_subparsers(dest = "command")

    add_parser = sub_parsers.add_parser("add", help = "Add a transaction")
    add_parser.add_argument("--amount", required=True, type = float, help = "Amount of transaction")
    add_parser.add_argument("--type", required=True, choices=["income", "expense"], help = "Type of transaction")
    add_parser.add_argument("--category", required=True, type = str, help = "Transaction category")
    add_parser.add_argument("--desc", required=True, type = str, help = "Description of the transaction")

    view_parser = sub_parsers.add_parser("view", help = "View the transactions")

    summary_parser = sub_parsers.add_parser("summary", help = "Give summary of transactions")

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