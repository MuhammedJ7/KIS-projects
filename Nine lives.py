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
