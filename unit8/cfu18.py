#Micah Kennedy
#1/7/2025
#Pd 1-2
#CFU 18

def version1():
    total = 0
    prices = [1.95,4.50,0.99,5.99]
    for i in range (len(prices)):
        total += prices[i]

    print(total)
def version2():
    total = 0
    prices = []
    num = int(input("How many prices do you want to add?: "))
    for i in range (num):
        price = float(input("What's the price of item " + str(i+1) + "?: "))
        prices.append(price)
    for i in range (len(prices)):
        total += prices[i]
    print("Total: " + str(total))
def version3():
    total = 0
    prices = []
    items = []
    num = int(input("How many items did you buy?: "))
    for i in range (num):
        item = input("What's the name of item " + str(i+1) + "?: ")
        price = float(input("What's the price of item " + str(i+1) + "?: "))
        prices.append(round(price,2))
        items.append(item)
    for i in range (len(prices)):
        total += prices[i]
    print("\nTini's Supermarket\n")
    for i in range (len(items)):
        print(items[i] + " ----- $" + str(prices[i]))
    print("Total: " + str(total))

version = int(input("Pick a version (1-3): "))
if version == 1:
    version1()
elif version == 2:
    version2()
elif version == 3:
    version3()
else:
    version = int(input("Pick a version (1-3): "))
