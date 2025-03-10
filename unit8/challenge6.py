'''
Micah Kennedy
Period 1-2
3/10/2025
Code Challenge 6
'''

def is_triangle(a,b,c):
    if (a+b>c) or (a+c>b) or (b+c>a):
        print("Yes")
    else:
        print("No")
        
def sticks():
    a = float(input("Enter stick length a: "))
    b = float(input("Enter stick length b: "))
    c = float(input("Enter stick length c: "))
    is_triangle(int(a),int(b),int(c))
    
sticks()
