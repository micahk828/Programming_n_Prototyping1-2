import simplegui
import random

def draw_handler(canvas):
    # your code goes here
    for i in range (1000):
     
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
      
        randRGBColor = "RGB( " + str(r) + "," + str(g) + "," + str(b) + ")"     
        
        x = random.randint(2, 600)
        y = random.randint(2, 600)

        canvas.draw_point((x, y), randRGBColor)

frame = simplegui.create_frame('Howdy - I love this program', 600, 600)
backg = "RGB( " + str(255) + "," + str(255) + "," + str(255) + ")"
frame.set_canvas_background(backg)

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
