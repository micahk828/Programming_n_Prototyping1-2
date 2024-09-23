#Micah Kennedy
#9/20/2024
#Pd1-2

print("Perimeter of a Rectangle")
length = int(input("Enter a number: "))
width = int(input("Enter a number: "))
perimeter = (2*length) + (2*width)
print("Perimeter of a " + str(length) + " x " + str(width) + " rectangle is " + str(perimeter))
print("Fahrenheit to Celsius")
temp = int(input("Enter a Fahrenheit temperature: "))
celsius = (temp - 32)*5/9
print(str(temp) + " degrees Fahrenheit is " + str(celsius) + " degrees Celsius")
print("The vertical distance of a projectile object")
velocity = int(input("Enter a number for vertical velocity: "))
time = int(input("Enter a number for time: "))
vertdist = velocity*time-((1/2*9)*(time**2))
print("The vertical distance of this projectile object is " + str(vertdist))
print("Distance between 2 points")
x1 = int(input("Enter a x value for one point: "))
y1 = int(input("Enter a y value for one point: "))
x2 = int(input("Enter a x value for a second point: "))
y2 = int(input("Enter a y value for a second point: "))
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The distance between " + str(x1) + "," + str(y1) + " and " + str(x2) + "," + str(y2) + " is " + str(distance))
