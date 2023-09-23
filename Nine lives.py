""", you have to guess the secret word one letter at a time. If your guess is wrong, you lose
a life."""

import random 

lives = 9
FantasyAdjectives = ['mythical','eerie','magic','supernatural', 'dreamlike', 'ethereal','fantastical','gothic','mytholgical',
                     'mystical','imaginary','dark', 'wonderful','enigmatic','fabulous','strange','beautiful','perplexing','dazzling',
                     'utopian','proud', 'brave']
words = ['pizza', 'fairy', 'teeth', 'shirt',
        'otter', 'plane']

secret.word = random.choice(words)
clue = list('?????')

heart_symbol = u'\u2764'

guessed_word_correctly = False

"""The main part of the code is a loop that gets a letter from the player and checks if it’s in the secret word. If it is, 
the code uses a function to update the clue. You’ll make that function, then create the main loop"""

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1