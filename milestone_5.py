import random

#Define class for hangman game

class Hangman:
    """
    A Hangman Game that asks the user for a letter and checks if it is in the chosen word.

    Parameters: 
    word_list: list
        List of words that can be used as the chosen word in the game
    num_lives:
        Number of lives the user has. This is a default parameter with value set to 5

    Attributes:
    ----------
    word: str
        The word to be guessed, picked randomly from the word_list
    word_guessed: list 
        A list of the letters of the word, with _ for each letter not yet guessed. 
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has.
    word_list: list
        A list of words
    list_of_guesses: list
        A list of the guesses that the user has already been tried

    Methods:
    ----------
    check_guess(guess)
        Checks if the letter guessed by the user is in the word
    ask_for_input()
        Asks the user for a letter
    """

    #define attributes
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)
    

    #function to check if the guessed letter is in the chosen word
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        guess = guess.lower()       
        
        if guess in self.word:

            #replace the '_' in word_guessed list with the guessed letter
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess

            #reduce number of unique letters left in the chosen word by one
            self.num_letters -= 1

            #print message to user
            print(f"Good guess! {guess} is in the word.")
            print(self.word_guessed)

        else:

            #reduce number of lives by one
            self.num_lives -= 1

            #print message to user
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
    

    #function to ask for input and run checks
    def ask_for_input(self):
        
        #keep asking the user to guess a letter, checking if the input is unique, valid and is in the chosen word
        while True:

            #ask user to guess a letter
            guess = input('Guess a letter: ')

            #check if input is valid
            if not len(guess)==1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue

            #check if guess has been tried before
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")
                continue

            #add guess to list of guesses and run check_guess method
            else:   
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break


#function to create an instance of the hangman class and add conditions to win the game
def play_game(word_list):
    
    num_lives = 5
    game = Hangman(word_list, num_lives)

    #game logic
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
        elif game.num_letters > 0:
            game.ask_for_input()
            continue
        else:
            print('Congratulations. You won the game!')
        break


#play the game
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)