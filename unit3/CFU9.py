#Micah Kennedy
#10/17/2024
#Pd1-2

import random
user_plays = int(input("How many rolls do you want to play? "))
total = 0
def guess():
    dice = random.randint(1,6)
    points = 0
    ans = int(input("Pick a number from 1-6: "))
    if ans == dice:
        points = points + 6
    else:
        points = points - 1
    key = "The answer was " + str(dice) + " you put " + str(ans)
    print(key)
    return points
total += guess()
if user_plays > 0:
    guess()
    user_plays = user_plays -1
    total += guess()
    print("Thanks for playing!!\nYour score is " + str(total))




