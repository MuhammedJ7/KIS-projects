"""In this project,
build a tool that makes secure, memorable passwords
to help keep your private information safe"""

"""This project will how to use Pythons random module. The program uses random choices from
groups of adjectives, nouns, numbers, and punctuation
characters to assemble each password"""

import random 
import string

FantasyAdjectives = ['mythical','eerie','magic','supernatural', 'dreamlike', 'ethereal','fantastical','gothic','mytholgical',
                     'mystical','imaginary','dark', 'wonderful','enigmatic','fabulous','strange','beautiful','perplexing','dazzling',
                     'utopian','proud', 'brave']

nouns = nouns = ["apple", "dog", "cat", "car", "house", "book", "computer", "flower", "friend", "city", "tree", "music",
                  "beach", "sun", "river", "mountain", "child", "school", "food", "movie", "job", "money", "time", "heart"]


print ('Welcome to your own personal password picker')


adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)
password = adjective + noun + str(number) + special_char

print('Your new password is: %s' % password)