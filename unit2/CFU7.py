#Micah Kennedy
#10/10/2024
#Pd 1-2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
def sum():
    s = num1 + num2 + num3
    print("The sum of the three numbers is: " + str(s))
    return s
sum()
def avg(x):
    avg = x/3
    print("The average of your three nummbers is: " + str(avg))
    return avg
avg(sum())
