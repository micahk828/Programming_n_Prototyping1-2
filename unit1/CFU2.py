#9/16/2024
#Micah Kennedy
#Pd 1-2

start = input("Click enter to create your profile")
fname = input("What is your first name")
lname = input("What is your last name")
age = input("How old are you?")
sleep = input("How many hours do you sleep?")

print(fname + "'s Profile\n\n" + "Name: " + fname, lname + "\nAge: " + age + " years old\n" + "Average Sleep: " + sleep + " hours")
print("You turn 21 in " + str(21-int(age)) + " years!")
