# Budget Tracker CLI

Project URL: https://roadmap.sh/projects/expense-tracker

## Overview
Budget Tracker is a command-line application that allows users to track their financial transactions. Users can add transactions, view them, get a summary of their income and expenses, and visualize their spending habits through a pie chart.

## Features
- Add transactions (income or expense) with category and description.
- View all recorded transactions in a tabular format.
- Get a summary of total income, total expenses, and balance.
- Visualize spending distribution with a pie chart.

## Requirements
- Python 3.x
- Required Python packages:
  - `argparse`
  - `csv`
  - `datetime`
  - `tabulate`
  - `matplotlib`

You can install missing dependencies with:
```bash
pip install tabulate matplotlib
```

## Installation
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/samarthjain2002/Projects.git
cd "Python Projects\CLI-Apps\Budget Tracker"
```

## Usage
The application is operated via the command line with the following commands:

### 1. Add a transaction
```bash
python "Budget Tracker.py" add --amount <amount> --type <income/expense> --category <category> --desc "description"
```
Example:
```bash
python "Budget Tracker.py" add --amount 1000 --type income --category Salary --desc "Monthly salary"
python "Budget Tracker.py" add --amount 200 --type expense --category Food --desc "Dinner at a restaurant"
```

### 2. View transactions
```bash
python "Budget Tracker.py" view
```

### 3. Get a summary
```bash
python "Budget Tracker.py" summarize
```

### 4. Visualize expenses
```bash
python "Budget Tracker.py" visualize
```
This will generate a pie chart showing spending by category.

## Data Storage
Transactions are stored in a CSV file named `budget_data.csv`. Each transaction is recorded with:
- Date & Time
- Amount
- Type (income/expense)
- Category
- Description

## License
This project is open-source and available under the MIT License.
