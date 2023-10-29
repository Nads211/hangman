#Task 1: Define a list of possible words
#Task 2: Choose random word

import random

word_list = ['apple', 'pear', 'orange', 'banana', 'grapes']
print(word_list)
word = random.choice(word_list)
print(word)

guess = input('Guess the first letter: ')

if len(guess)==1 and guess.isalpha():
    print('Good Guess')
else:
    print('Oops! That is not a valid input')

