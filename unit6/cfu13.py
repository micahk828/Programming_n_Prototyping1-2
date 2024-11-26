#Micah Kennedy
#CFU 13
#11/26/2024
#Pd 1-2

import simplegui

def draw_handler(canvas):
    #Face
    canvas.draw_point([100, 50], "white")
    canvas.draw_point([110, 55], "white")
    canvas.draw_point([120, 65], "white")
    canvas.draw_point([125, 75], "white")
    canvas.draw_point([130, 85], "white")
    canvas.draw_point([130, 115], "white")
    canvas.draw_point([125, 125], "white")
    canvas.draw_point([120, 135], "white")
    canvas.draw_point([110, 145], "white")
    canvas.draw_point([100, 150], "white")
    canvas.draw_point([90, 145], "white")
    canvas.draw_point([80, 135], "white")
    canvas.draw_point([75, 125], "white")
    canvas.draw_point([70, 115], "white")
    canvas.draw_point([70, 85], "white")
    canvas.draw_point([75, 75], "white")
    canvas.draw_point([80, 65], "white")
    canvas.draw_point([90, 55], "white")
    #Left Eye
    canvas.draw_point([85, 95], "white") 
    canvas.draw_point([86, 96], "white")
    canvas.draw_point([87, 95], "white")
    canvas.draw_point([86, 94], "white")
    #Right Eye
    canvas.draw_point([115, 95], "white") 
    canvas.draw_point([116, 96], "white")
    canvas.draw_point([117, 95], "white")
    canvas.draw_point([116, 94], "white")
    #Smile
    canvas.draw_point([95, 125], "white")
    canvas.draw_point([96, 126], "white")
    canvas.draw_point([97, 127], "white")
    canvas.draw_point([98, 128], "white")
    canvas.draw_point([99, 129], "white")
    canvas.draw_point([100, 130], "white")
    canvas.draw_point([101, 129], "white")
    canvas.draw_point([102, 128], "white")
    canvas.draw_point([103, 127], "white")
    canvas.draw_point([104, 126], "white")
    canvas.draw_point([105, 125], "white")
frame = simplegui.create_frame("CFU 13: Happy Dots", 200, 200)
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler)
frame.start()
