#Micah Kennedy
#Pd 1-2
#11/27/2024

import simplegui

def draw_handler(canvas):
    # Face
    canvas.draw_circle((100, 100), 80, 2, "white")
    
    # Left Eye
    canvas.draw_circle((70, 80), 15, 2, "white")
    canvas.draw_circle((70, 80), 5, 10, "white")
    
    # Right Eye
    canvas.draw_circle((130, 80), 15, 2, "white")
    canvas.draw_circle((130, 80), 5, 10, "white")
    
    # Smile
    canvas.draw_circle((100, 110), 50, 2, "white")
    canvas.draw_circle((100, 90), 50, 20, "black")


frame = simplegui.create_frame("CFU 16: Happy Circles", 200, 200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()
