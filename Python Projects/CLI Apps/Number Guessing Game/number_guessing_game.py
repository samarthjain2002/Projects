import random


def main():
    while True:
        rand_num = random.randint(1, 100)

        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.\n")

        print("Please select the difficulty level:")
        print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
        difficulty = int(input("Enter your choice: "))

        if difficulty == 1:
            difficulty = "Easy"
            chances = 10
        elif difficulty == 2:
            difficulty = "Medium"
            chances = 5
        else:
            difficulty = "Hard"
            chances = 3
        print(f"\nGreat! You have selected the {difficulty} difficulty level.")
        print(f"You have {chances} chances to guess the correct number.")
        print("Let's start the game!\n")


        guessFlag = False
        for i in range(chances):
            guess = int(input("Enter your guess: "))

            if guess == rand_num:
                guessFlag = True
                break
            elif guess > rand_num:
                print(f"Incorrect! The number is less than {guess}.\n")
            else:
                print(f"Incorrect! The number is greater than {guess}.\n")

        if guessFlag:
            print(f"Congratulations! You guessed the correct number in {i + 1} attempts.")
        else:
            print(f"The number is {rand_num}.\n")
            YRN = input("Would you like to play another round?: Y/y for yes, N/n for no: ")
            if YRN in "nN":
                break


if __name__ == "__main__":
    main()