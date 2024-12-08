import simplegui
import random
x=-20
def draw_handler(canvas):
    global x
    x = x + 5
    y=random.randint(25,100)
    canvas.draw_circle((x, 200), 50, 1, "blue", "blue")
    canvas.draw_circle((x-80, 275), 50, 1, "red", "red")
    canvas.draw_circle((x-y, 350), 50, 1, "yellow", "yellow")
    canvas.draw_line([x,x],[x-x,500], 4, "white")
    canvas.draw_line([500,x-x], [x,x], 4, "white")
    if x > 620:
        x=-20


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("skyblue")
frame.set_draw_handler(draw_handler)
frame.start()
