#Micah Kennedy
#9/23/2024
#Pd 1-2

import math
name = input("What is your name?")
print("Hi, ", name + "!")
a = int(input("Enter a value for the a coeficient: "))
b = int(input("Enter a value for the b coeficient: "))
c = int(input("Enter a value for the c coeficient: "))
print("Your equation is " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
x1 = (-b + math.sqrt((b**2 - (4*a*c))))/(2*a)
x2 = (-b - math.sqrt((b**2 - (4*a*c))))/(2*a)
print("The roots of this quadratic equation are x = " + str(x1) + " and x = " + str(x2))
