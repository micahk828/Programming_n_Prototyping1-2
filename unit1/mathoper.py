#Micah Kennedy
#9/23/2024
#Pd 1-2

'''
    This program calculates the perimeter of a 
    rectangle using input from the user.
'''

#Getting the length from the user
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))

perimeter = 2 * (length + width)

print("The perimeter is " + str(perimeter))
