#Micah Kennedy
#10/21/2024
#Pd1-2

import random

print("Welcome to the Number Guessing Game!")
ranNum = random.randint(1, 10)

def guess_number(ranNum, attempts=0):
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == ranNum:
        print("It took you " + str(attempts) + " attempts")
        return
    else:
        if guess > ranNum:
            print("Too High")
        else:
            print("Too Low")
        guess_number(ranNum, attempts)


guess_number(ranNum)
