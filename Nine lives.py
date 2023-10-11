""", you have to guess the secret word one letter at a time. If your guess is wrong, you lose
a life."""

import random 

lives = 9
FantasyAdjectives = ['mythical','eerie','magic','supernatural', 'dreamlike', 'ethereal','fantastical','gothic','mytholgical',
                     'mystical','imaginary','dark', 'wonderful','enigmatic','fabulous','strange','beautiful','perplexing','dazzling',
                     'utopian','proud', 'brave']
words = ['pizza', 'fairy', 'teeth', 'shirt','otter', 'plane','brush','horse','light']

secret_word = random.choice(words)
clue = [] #Words of varying length
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1

heart_symbol = u'\u2764'

guessed_word_correctly = False

"""The main part of the code is a loop that gets a letter from the player and checks if it’s in the secret word. If it is, 
the code uses a function to update the clue. You’ll make that function, then create the main loop"""

def update_clue(guessed_letter, secret_word, clue):
    index = 0

    """If a letter matches, the program inserts it into the clue, using index to find the right position in the list of
question marks."""
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

difficulty = input('Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3  Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
elif difficulty ==3:
    lives = 6


while lives > 0:
    print (clue)
    print('Lives left: '+ heart_symbol*lives) #repeating a string
    guess = input("Guess a letter or if you want, the whole word ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else: 
        print ("Sorry but that is incorrect, you lost a life ")
        lives =lives-1
        
if guessed_word_correctly : 
    print("Well done , you won! The secret word was" + secret_word)
else :
    print("Oh no you lost, the secret word was "+ secret_word)

