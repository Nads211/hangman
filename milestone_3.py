#%%
import random

#Create word list and select a random word
word_list = ['apple', 'pear', 'orange', 'banana', 'grapes']
word = random.choice(word_list)
print("Target word is: " + word)

#define function to check if the guessed letter is in the target word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    #Iteratively check if the input is a valid guess
    while True:
        guess = input('Guess a letter: ')
        if len(guess)==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    #check if guess is in word
    check_guess(guess)

ask_for_input()

#%%

# %%
