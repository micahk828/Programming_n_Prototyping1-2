#Micah Kennedy
#10/25/2024
#Pd 1-2

print("Check out these functions!\n")
pick = int(input("Enter 1 for Count by 10, 2 for Decimals, 3 for Bottles of Beer "))

def counting():
    print("Counting by 10")
    for x in range(10,80,10):
        print(x)
    
   
def decimals(): 
    print("Exploring Decimals")
    for y in range(0,10,1):
        print(y)
        y=y+0.5
        print(y)
    print(y+0.5)


def bottles():
    print("99 Bottles of Beer Song")
    num = 99   
    for z in range(99, 1, -1):
        print(str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer.\nTake one down and pass it around, " + str(num-1) + " bottles of beer on the wall.\n")
        num -= 1
        if num == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
        
if pick == 1:
    counting()
if pick == 2:
    decimals()
if pick == 3:
    bottles()
