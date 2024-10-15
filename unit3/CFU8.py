#Micah Kennedy
#10/15/2024
#Pd1-2

#version 1
deli = input("Did you order delivery? ")
if deli == "yes":
    print("Great!")
else:
    print("No?! So who is cooking?")
#version 2    
deli = input("Did you order delivery? ")
if deli == "yes":
    print("Great!")
    cost = float(input("What is the cost of the food ordered? "))
    people = int(input("How many people are splitting the bill? "))
    cpp = cost/people
    print("The cost per person is $" + str(cpp))
else:
    print("No?! So who is cooking?")
