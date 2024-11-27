#Micah Kennedy
#Pd 1-2
#11/27/2024

import simplegui

def draw_handler(canvas):
    # Face 
    canvas.draw_polygon([(50, 100), (70, 50), (120, 30), (170, 50), (190, 100), (170, 150), (120, 170), (70, 150)], 2, "white")
    
    # Left Eye
    canvas.draw_polygon([(90, 80), (100, 80), (100, 90), (90, 90)], 2, "white")
    
    # Right Eye
    canvas.draw_polygon([(140, 80), (150, 80), (150, 90), (140, 90)], 2, "white")
    
    # Smile
    canvas.draw_polygon([(80, 130), (120, 150), (160, 130)], 2, "white")

frame = simplegui.create_frame("CFU 15: Happy Shapes", 250, 200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()
