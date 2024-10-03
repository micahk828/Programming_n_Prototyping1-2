#Micah Kennedy
#10/02/2024
#Pd1-2

import math
import random
ranNum = random.randint(1,100)
userNum = int(input("Enter a number: "))
'''
The sum of the random number and the user's number.
The difference (random number - user number).
The product of the random number and the user's number.
The quotient of the random number divided by the user's number.
The remainder of the random number divided by the user's number (using the modulo operator).
The square root of the random number (using math.sqrt()).
The user’s number raised to the power of the random number (using math.pow()).
Print the random number, the user's number, and the results of the calculations in a clear format.
'''
Sum = ranNum + userNum
diff = ranNum - userNum
mult = ranNum * userNum
divi = ranNum // userNum
modu = ranNum % userNum
sqro = math.sqrt(ranNum)
power = math.pow(userNum, ranNum)

print("The sum is " + str(Sum))
print("The difference is " + str(diff))
print("The product is " + str(mult))
print("The quotient is " + str(divi))
print("The remainder is " + str(modu))
print("The square root of the computer's number is " + str(sqro))
print("Your number raised to the computer's number is " + str(power))
