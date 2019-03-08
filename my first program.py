# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:42:53 2019

@author: Palash Mondal
"""

import random
rng=random.Random()
number=rng.randrange(1,1000)  #get random number between 1 and 1000
guesses=0
#message=' '
while True:
    guess=int(input( "\nGuess my number between 1 and 1000: "))
    guesses+=1
    if guess > number:
        print("\n"+str(guess) + " is too high.")
    elif guess<number:
        print("\n"+str(guess) + " is too low.")
    else:
        break
print("\n\nGreat, you got it in " + str(guesses) + " guesses!")   
            