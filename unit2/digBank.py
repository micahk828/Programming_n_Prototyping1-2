#Micah Kennedy
#9/30/2024
#Pd1-2

'''
Little Canadian kid broke their piggy bank
you are to create a program to help them 
figure out how much money they have
pennies = 1¢
nickles = 5¢
dimes = 10¢
quarters = 25¢
loonies = 1$ or 100¢
toonies = 2$ or 200¢
ask the kid how many coins they of each
calculate the total and give answer in 
decimals and in a combination
i.e. $13.67 or $13 and 2 quarters, 1 dime, 1 nickel, 2¢
'''
print("My Digital Bank")
pennies = int(input("How many pennies do you have?"))
nickles = int(input("How many nickels do you have?"))                                                                                                      
dimes = int(input("How many dimes do you have?"))
quarters = int(input("How many quarters do you have?"))
loonies = int(input("How many loonies do you have?"))
toonies = int(input("How many toonies do you have?"))
total = (pennies + (nickles*5) + (dimes*10) + (quarters*25) + (loonies * 100) + (toonies*200))/100
print("Total: $" + str(total) + "\nThe Breakdown\n$" + str(2*toonies + loonies) + " and " + str(quarters) + " quarters and " + str(dimes) + " dimes and " + str(nickles) + " nickles and " + str(pennies) + "¢\nGood Money Managing, kid!!")
