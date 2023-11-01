import random

#Define class
class Hangman:
    """
    Agruments: word_list and num_lives as parameters. num_lives is a default parameter and set the value to 5.

    Hangman attributes:
    word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
    word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int - The number of lives the player has at the start of the game.
    word_list: list - A list of words
    list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
    """
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        for element in self.word: self.word_guessed.append('_')
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    #define function to check if the guessed letter is in the target word
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter==guess:
                    position = self.word.index(letter)
                    self.word_guessed[position] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")
    
    #Function to ask for input
    def ask_for_input(self):
        #Iteratively check if the input is a valid guess
        while True:
            guess = input('Guess a letter: ')
            if not len(guess)==1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:   
                #check if guess is in word
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ['apple', 'pear']#, 'orange', 'banana', 'grapes']

#hangman = Hangman(word_list)
#hangman.ask_for_input()


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratz, you won')

play_game(word_list)