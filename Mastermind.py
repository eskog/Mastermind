#!/usr/bin/python

import random
chosenNumbers = []
correctGuesses = 0;
for x in range(0,4):
    #print(random.randint(0,10))
    chosenNumbers.append(random.randint(0, 9))
solved = False
while not solved:
    guess = raw_input("Enter your guess")
    try:
        intconvert = int(guess)
    except:
        raise
    else:
        guessedNumber = list(guess)
        for y in range(0,4):
                #if int(guessedNumber[y]) == chosenNumbers[x]:
            if chosenNumbers[y] == int(guessedNumber[y]):
                correctGuesses += 1
        if correctGuesses == 4:
            print("You have found all the correct numbers")
            solved = True
        else:
            print("*" * correctGuesses)
            correctGuesses = 0