'''
Micah Kennedy
Pd 1-2
3/6/2025
Code Challenge 5
'''

print("Fernat's Last Theorem Test")
def check_fermat(a,b,c,n):
    if n>2:
        if (a**n + b**n) == (c**n):
            print("Holy smokes, Fernat was wrong!")
        else:
            print("No, that doesn't work.")
    else:
        print("The variable n is not greater than 2.")
        
check_fermat(a,b,c,n)
