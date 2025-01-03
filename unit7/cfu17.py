# Micah Kennedy
# 1-2
# 01/02/25
# CFU 17 Review + BuiltIn Functions

box = "Beignet"
def formating(box):
    userInput = int(input("Choice? (1,2,3,4,5,6,7)"))
    if userInput == 1:
        #Capitalize the first letter of the string
        print(box.capitalize())
    elif userInput == 2:
        #Find and return the position of a value in the string
        print(box.find("i"))
    elif userInput == 3:
        #Return true if the variable is a number
        print(box.isdigit())
    elif userInput == 4:
        #Output the variable all lowercase
        print(box.lower())
    elif userInput == 5:
        #Output the variable all uppercase
        print(box.upper())
    elif userInput == 6:
        #Replace am index item for another item
        print(box.replace("o", "i"))
    else:
        print("Not a valid option")

formating(box)
