import string
import random

import argparse

import os


HISTORY_FILE = "password_history.txt"

def password_generator(length = 12, strength = 'strong'):
    if strength == 'weak':
        chars = string.ascii_lowercase
    elif strength == 'medium':
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return file.read().splitlines()
    return []


def save_history(password):
    with open(HISTORY_FILE, "a") as file:
        file.write(password + "\n")


def check_password_strength(password):
    length_criteria = len(password) >= 12
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        print("The password strength is strong")
    elif all([length_criteria, uppercase_criteria or lowercase_criteria, digit_criteria]):
        print("The password strength is medium")
    else:
        print("The password strength is weak")
 

def main():
    history = load_history()
    
    parser = argparse.ArgumentParser(description = "Password Generator CLI")

    parser.add_argument("--length", type = int, default = 12, help = "Password length")
    parser.add_argument("--strength", type = str, choices = ["weak", "medium", "strong"], default = "strong", help = "Password strength")
    parser.add_argument("--history", action = "store_true", help = "Show all passwords generated during this session")
    parser.add_argument("--interactive", action = "store_true", help = "Start the interactive menu")

    args = parser.parse_args()

    if args.history:
        if history:
            print("The password history")
            for i, pwd in enumerate(history, 1):
                print(f"{i}: {pwd}")
        else:
            print("No passwords generated")
        return
    
    if args.interactive:
        print("Interactive mode enabled")
        while True:
            print("\nMenu:")
            print("1. Generate Password")
            print("2. View Password History")
            print("3. Check Password Strength")
            print("4. Exit")
            
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    length = int(input("Enter password length: "))
                    strength = input("Enter password strength (weak/medium/strong): ").lower()
                    password = password_generator(length, strength)
                    history.append(password)
                    save_history(password)
                    print(f"Generated Password: {password}")
                case 2:
                    if history:
                        print("The password history")
                        for i, pwd in enumerate(history, 1):
                            print(f"{i}: {pwd}")
                    else:
                        print("No passwords generated")
                case 3:
                    password = input("Enter the password to be checked: ").strip()
                    check_password_strength(password)
                case 4:
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid choice")

    password = password_generator(args.length, args.strength)
    history.append(password)
    save_history(password)
    print("Generated password: " + password)



if __name__ == "__main__":
    main()