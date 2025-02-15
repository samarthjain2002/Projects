# Number Guessing Game

Project URL: https://roadmap.sh/projects/number-guessing-game
A simple command-line-based Number Guessing Game built with Python. The game randomly selects a number between 1 and 100, and the player must guess the correct number within a limited number of attempts.

## Features
- Three difficulty levels:
  - **Easy:** 10 attempts
  - **Medium:** 5 attempts
  - **Hard:** 3 attempts
- Hints provided after each incorrect guess.
- Option to play another round after the game ends.

## How to Play
1. Run the script using Python.
2. Choose a difficulty level.
3. Enter guesses until you find the correct number or run out of attempts.
4. Get feedback after each guess.
5. Play again if you want!

## Installation & Running the Game
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone the repository or download the script.
2. Navigate to the script's directory.
3. Run the following command:
   ```sh
   python number_guessing_game.py
   ```

## Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2

Great! You have selected the Medium difficulty level.
You have 5 chances to guess the correct number.
Let's start the game!

Enter your guess: 50
Incorrect! The number is greater than 50.

Enter your guess: 75
Incorrect! The number is less than 75.

Enter your guess: 62
Congratulations! You guessed the correct number in 3 attempts.
```

## Enhancements & Future Improvements
- Implement a scoring system.
- Add a graphical user interface (GUI).
- Store game statistics for multiple rounds.

## Contributing
Feel free to fork this repository and contribute improvements or new features!

## License
This project is licensed under the MIT License.

