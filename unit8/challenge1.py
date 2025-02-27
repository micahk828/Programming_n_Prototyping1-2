'''
Micah Kennedy
Pd 1-2
Coding Practice
'''

def code1():
    import math  # Import the math module for mathematical operations
    def sphereVolume(radius):
        volume = (4/3) * math.pi * (radius**3) # Calculate the volume of a sphere using the formula V = (4/3) * π * r^3
        return volume  # Return the calculated volume
    volume_result = sphereVolume(5)  # Calculate the volume for a sphere with radius 5
    print("The volume a sphere with radius 5 is " + str(volume_result))  # Print the result

def code2():
    def w_cost(copies):
        cover_price = 24.95  # Set the cover price of the book
        discount = 0.40  # Set the discount percentage
        shipFirst = 3  # Set the shipping cost for the first book
        shipAfter = 0.75  # Set the shipping cost for each additional book
        discountPrice = cover_price * (1 - discount)  # Calculate the discounted price
        totalbookcost = discountPrice * copies  # Calculate the total cost of books
        shippingcost = shipFirst + (shipAfter * (copies - 1))  # Calculate the total shipping cost
        total = shippingcost + totalbookcost  # Calculate the total cost including shipping
        print(f"Your total is ${total:.2f}")  # Print the total cost formatted to 2 decimal places
    w_cost(60)  # Calculate the wholesale cost for 60 copies

def code3():
    def running_time(start_hour, start_minutes):
        easy_pace = 8 * 60 + 15  # Convert easy pace to seconds
        tempo_pace = 7 * 60 + 12  # Convert tempo pace to seconds
        total_time_seconds = easy_pace * 2 + (tempo_pace * 3)  # Calculate total running time in seconds
        total_minutes = total_time_seconds // 60  # Convert total time to minutes
        total_seconds = total_time_seconds % 60  # Calculate remaining seconds
        end_minutes = total_minutes + start_minutes  # Calculate end minutes
        end_hour = start_hour  # Initialize end hour
        if end_minutes >= 60:  # Adjust hour and minutes if minutes exceed 60
            end_hour += end_minutes // 60
            end_minutes = end_minutes % 60
        return end_hour, end_minutes  # Return the end time
    
    end_hour, end_minutes = running_time(6, 52)  # Calculate arrival time starting at 6:52 AM
    print(f"You will arrive home for breakfast at {end_hour}:{end_minutes} AM.")  # Print the arrival time

code1()  # Execute code1 function
code2()  # Execute code2 function
code3()  # Execute code3 function
