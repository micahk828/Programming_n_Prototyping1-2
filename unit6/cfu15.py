#Micah Kennedy
#Pd 1-2
#11/27/2024

import simplegui

def draw_handler(canvas):
    # Face 
    canvas.draw_polygon([(35, 100), (55, 50), (105, 30), (155, 50), (175, 100), (155, 150), (105, 170), (55, 150)], 2, "white")
    
    # Left Eye
    canvas.draw_polygon([(75, 80), (85, 80), (85, 90), (75, 90)], 2, "white")
    
    # Right Eye
    canvas.draw_polygon([(125, 80), (135, 80), (135, 90), (125, 90)], 2, "white")
    
    # Smile
    canvas.draw_polygon([(65, 130), (105, 150), (145, 130)], 2, "white")

frame = simplegui.create_frame("CFU 15: Happy Shapes", 200, 200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()
