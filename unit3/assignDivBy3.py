#Micah Kennedy
#10/31/2024
#Pd1-2

check = int(input("How many numbers do you need to check? "))
div = 0
indiv = 0
for i in range(check):
    num = int(input("Enter number: "))
    if (num % 3) == 0:
        div += 1
        print(str(num) + " is divisible by 3.")
    else:
        indiv += 1
        print(str(num) + " is not divisible by 3.")
print("You entered " + str(div) + " number(s) that are divisible by 3.")
print("You entered " + str(indiv) + " number(s) that are not divisible by 3.")
