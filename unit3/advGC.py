#Micah Kennedy & Nataly Parache
#10/22/2024
#Pd 1-2

import random
import time

print("Welcome to the Number Guessing Game!")
rounds = int(input("How many rounds do you want to play? "))
diff = int(input("How hard do you want it to be? (1-3) "))
start = time.time()

if diff == 3:
    secNum = 1000
elif diff == 2:
    secNum = 50
else:
    secNum = 10

totAttempts = 0
roundNum = 1

def guess_number(attempts, ranNum):
    attempts += 1
    guess = int(input("Guess a number between 1 and " + str(secNum) + ": "))
    if guess == ranNum:
        print("Correct! It took you " + str(attempts) + " attempts.")
        return attempts
    elif guess > ranNum:
        print("Too high!")
        return guess_number(attempts, ranNum)
    else:
        print("Too low!")
        return guess_number(attempts, ranNum)

def start_round(roundNum, totAttempts):
    if roundNum > rounds:
        average = totAttempts / rounds
        end = time.time()
        print("\nYou made " + str(totAttempts) + " attempts in total.")
        print("You played for " + str(round(end - start, 0)) + " seconds.")
        print("Average attempts per round = " + str(round(average, 1)))
    else:
        print("\nRound " + str(roundNum))
        ranNum = random.randint(1, secNum)
        attempts = guess_number(0, ranNum)
        totAttempts += attempts
        start_round(roundNum + 1, totAttempts)

start_round(roundNum, totAttempts)
