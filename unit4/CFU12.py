#Micah Kennedy
#10/29/2024
#Pd 1-2


def vers1():
    entry = input("Enter your password: ")
    while entry != "simonnyc":
        print("Wrong Password")
        entry = input("Enter your password: ")
    print("Correct! You may enter")


def vers2():
    entry = input("Enter your password: ")
    attempts=1
    while entry != "simonnyc" and attempts < 3:
        print("Wrong Password")
        attempts += 1
        entry = input("Enter your password: ")
        if attempts >= 3:
            print("Too many bad attempts")
    if entry == "simonnyc": 
        print("Correct! You may enter -->")

def main():
    vers = int(input("Enter 1 for Version 1 or 2 for Version 2: "))
    if vers == 1:
        vers1()
    elif vers == 2:
        vers2()
    else:
        main()
main()
