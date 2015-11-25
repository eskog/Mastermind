#!/usr/bin/python

import random
chosenNumbers = []
correctGuesses = 0;
guessCount = 0;
for x in range(0,4):
    #print(random.randint(0,10))
    chosenNumbers.append(random.randint(0, 9))
solved = False
while not solved:
    correctAnswers = ['-','-','-','-']
    guess = raw_input("Enter your guess: ")
    try:
        intconvert = int(guess)
    except:
        raise
    else:
        guessedNumber = list(guess)
        for y in range(0,4):
            if chosenNumbers[y] == int(guessedNumber[y]):
                correctGuesses += 1
                correctAnswers[y] = '*'
        if correctGuesses == 4:
            guessCount += 1
            print("You have found all the correct numbers in {0} guesses").format(guessCount)
            solved = True
        else:
            #print("*" * correctGuesses)
            print(correctAnswers)
            correctGuesses = 0
            guessCount += 1