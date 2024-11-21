import sqlite3
import os

# Function to create a database and table
def create_db():
    # Create or connect to a SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('example.db')  # SQLite file is created in the current directory
    cursor = conn.cursor()

    # Create a table if it doesn't exist already
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_user(name, age):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))

    conn.commit()
    conn.close()

# Function to query and display users
def display_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    print("Users in the database:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

    conn.close()

# Command-line interface
def cli():
    while True:
        print("\nSQLite CLI App")
        print("1. Create Database and Table")
        print("2. Add User")
        print("3. Display Users")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            create_db()
            print("Database and table created.")
        elif choice == '2':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            insert_user(name, age)
            print("User added.")
        elif choice == '3':
            display_users()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    cli()
