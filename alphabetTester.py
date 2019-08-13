#! python3

import random, sys

alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
    'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

reversedAlphabet = dict((v,k) for k,v in alphabet.items())
exitKeyword = 'exit'

def guessRelatedNumber():
    while True:
        letter = random.choice(list(alphabet))
        userInput = input("What is the number for '" + letter + "'?\n")

        if userInput == exitKeyword:
            break

        try:
            guess = int(userInput)
            number = alphabet[letter]

            if number == guess:
                print("Correct!\n")
            else:
                print("Incorrect, " + letter + " = " + str(number) + "\n")
        except ValueError:
            print("Please enter a number between 1 and 26.\n")

def guessRelatedLetter():
    while True:
        number = random.choice(list(reversedAlphabet))
        userInput = input("What is the letter for '" + str(number) + "'?\n")

        if userInput == exitKeyword:
            break

        try:
            guess = userInput
            letter = reversedAlphabet[number]

            if letter == guess:
                print("Correct!\n")
            else:
                print("Incorrect, " + str(number) + " = " + letter + "\n")
        except ValueError:
            print("Please enter a letter between 'a' and 'z'.\n")

def train():
    print("Welcome to the alphabet trainer. Type " + exitKeyword + " to stop.")
    print("In which mode do you want to train?\n")

    userInput = input("Type 1 for guessing numbers, type 2 for letters.\n")
    if userInput == exitKeyword:
        sys.exit()

    try:
        userChoice = int(userInput)
        if userChoice == 2:
            guessRelatedLetter()
        elif userChoice == 1:
            guessRelatedNumber()
        else:
            print('No valid choice given. Exiting program.')
            sys.exit()
    except ValueError:
        print('No valid choice given. Exiting program.')
        sys.exit()

train()
