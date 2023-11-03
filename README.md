# Hangman

### A simple hangman game in python. Made as part of the AI Core Data Analytics program.


Hangman is a classic game in which the computer selects word and the user tries to guess that word within a certain amount of attempts.


## File Structure

The complete hangman game can be found in ***milestone_5.py*** file.

The other files are task milestones as instructed by the AI Core program, and they build the foundations of the code used in the final game.

## How to Play
Navigate to ***milestone_5.py*** and click run!

Customisations: 
- You can edit the `word_list` variable to change the list of words that the game can choose from
- You can change the number of lives to make the game easier/harder by editing the `num_lives` variable in `play_game()` function

No special installations required.


## Key methods and functions:

> `Hangman`: class  
Defines attributes and methods for the hangman game. Full list of attributes and methods can be seen by viewing the class docustrings using `help(Hangman)`.

> `check_guess(guess)`: method  
Takes in a guessed letter as parameter and checks if it is in the chosen word

> `ask_for_input()`: method  
Gets the first guess from the user, validates the input, and runs the `check_guess(guess)` method.

> `play_game()`: function  
Initialises the hangman game. It creates an instance of the `Hangman` class and runs the `ask_for_input()` method until either the word has been guessed or you have run out of lives.


