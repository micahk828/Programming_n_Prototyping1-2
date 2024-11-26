#Micah Kennedy
#CFU 14
#11/26/2024
#Pd 1-2

import simplegui

def draw_handler(canvas):
    #Face
    canvas.draw_line([50, 100], [60, 70], 2, "white")
    canvas.draw_line([60, 70], [80, 50], 2, "white")
    canvas.draw_line([80, 50], [100, 40], 2, "white")
    canvas.draw_line([100, 40], [120, 50], 2, "white")
    canvas.draw_line([120, 50], [140, 70], 2, "white")
    canvas.draw_line([140, 70], [150, 100], 2, "white")
    canvas.draw_line([150, 100], [140, 130], 2, "white")
    canvas.draw_line([140, 130], [120, 150], 2, "white")
    canvas.draw_line([120, 150], [100, 160], 2, "white")
    canvas.draw_line([100, 160], [80, 150], 2, "white")
    canvas.draw_line([80, 150], [60, 130], 2, "white")
    canvas.draw_line([60, 130], [50, 100], 2, "white")
    #Left Eye
    canvas.draw_line([85, 85], [90, 85], 2, "white")
    canvas.draw_line([85, 85], [85, 90], 2, "white")
    canvas.draw_line([90, 85], [90, 90], 2, "white")
    canvas.draw_line([85, 90], [90, 90], 2, "white")
    #Right Eye
    canvas.draw_line([110, 85], [115, 85], 2, "white")
    canvas.draw_line([110, 85], [110, 90], 2, "white")
    canvas.draw_line([115, 85], [115, 90], 2, "white")
    canvas.draw_line([110, 90], [115, 90], 2, "white")
    #Smile
    canvas.draw_line([95, 125], [100, 130], 2, "white")
    canvas.draw_line([100, 130], [105, 125], 2, "white")
    
frame = simplegui.create_frame("CFU 14: Happy Lines", 200, 200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()
