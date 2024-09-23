import math
r = int(input("What is the radius of your cylinder?"))
height = int(input("What is the height of your cylinder?"))
vol = height*math.pi*r**2
volume = round(vol)
print("Volume of a Cylinder:")
print("Volume is",volume)
