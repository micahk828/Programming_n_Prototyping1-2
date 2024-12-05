import simplegui

def draw_handler(canvas):
    # your code goes here
    canvas.draw_circle([300,300],280,1,"black","white")
    canvas.draw_circle([300,300],210,1,"black","blue")
    canvas.draw_circle([300,300],140,1,"black","red")
    canvas.draw_circle([300,300],70,1,"black","yellow")
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
