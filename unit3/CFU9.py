#Micah Kennedy
#10/17/2024
#Pd1-2

import random
user_plays = int(input("How many rolls do you want to play? "))
dice = 0
def guess():
    dice = random.randint(1,6)
    ans = int(input("Pick a number from 1-6: "))
    global points
    points = 0
    if ans == dice:
        points = points + 6
    else:
        points = points - 1
for _ in range(user_plays):
    guess()

print("Your score is " + str(points))
