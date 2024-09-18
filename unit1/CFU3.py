#Micah Kennedy
#9/17/2024
#Pd1-2

fname = input("What's your first name?")
lname = input("What's your last name?")
print("Hey, " + fname,lname + "!!\n")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print("The 5 Mathematical Operations:\n")
#Calculations
result1 = number1 + number2
result2 = number1 - number2
result3 = number1 * number2
result4 = number1 / number2
result5 = number1 % number2

print(str(number1) + " + " + str(number2) + " = " + str(result1))
print(str(number1) + " - " + str(number2) + " = " + str(result2))
print(str(number1) + " * " + str(number2) + " = " + str(result3))
print(str(number1) + " / " + str(number2) + " = " + str(result4))
print(str(number1) + " % " + str(number2) + " = " + str(result5))
