#Micah Kennedy
#10/2/2024
#Pd1-2

sideA = int(input("Enter side A: "))
sideB = int(input("Enter side B: "))
sideC = int(input("Enter side C: "))
sideD = int(input("Enter side D: "))
sideE = int(input("Enter side E: "))
rect1 = sideA*sideB
rect2 = (sideA - sideC) * (sideD - sideB - sideE)
tri1 = 0.5 * (sideA - sideC) * sideE
print("Room Area: " + str(rect1+rect2+tri1))
