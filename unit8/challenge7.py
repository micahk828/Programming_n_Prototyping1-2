'''
Micah Kennedy
Pd 1-2
Code Challenge 7
'''

import simplegui

# Create a Turtle-like simulator
#Google Base code below
class Turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.path = [(x, y)]

    def forward(self, distance):
        from math import cos, sin, radians
        self.x += distance * cos(radians(self.angle))
        self.y += distance * sin(radians(self.angle))
        self.path.append((self.x, self.y))

    def right(self, angle):
        self.angle += angle

# Function to draw a square using the turtle
def square(t):
    for _ in range(4):
        t.forward(100)  # Move forward 100 pixels
        t.right(90)     # Turn right 90 degrees

# Function to draw the turtle's path on the canvas
def draw(canvas):
    if len(bob.path) > 1:
        canvas.draw_polygon(bob.path, 5, "White")

bob = Turtle(100, 100)

square(bob)

# Create a frame
frame = simplegui.create_frame("Turtle Square", 400, 400)

# Set the draw handler
frame.set_draw_handler(draw)

# Start the frame
frame.start()


'''
Google Turtle Simulator
import math

class Turtle:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle  # in degrees
        self.path = [(x, y)]

    def forward(self, distance):
        rad_angle = math.radians(self.angle)
        self.x += distance * math.cos(rad_angle)
        self.y += distance * math.sin(rad_angle)
        self.path.append((self.x, self.y))

    def backward(self, distance):
         self.forward(-distance)

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle

    def get_position(self):
        return self.x, self.y
    
    def get_path(self):
      return self.path

# Example usage
my_turtle = Turtle()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(50)
print(my_turtle.get_position()) # Output: (50.0, 100.0)
print(my_turtle.get_path()) # Output: [(0, 0), (100.0, 0.0), (100.0, 50.0)]
'''
