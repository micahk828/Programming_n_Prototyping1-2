import simplegui

def draw_handler(canvas):
    for i in range (4):
        canvas.draw_line([300,0+110*i],[0+110*i,300], 5, "white")
        canvas.draw_line([0+110*i,300],[300,600-110*i], 5, "white")
        canvas.draw_line([300,600-110*i],[600-110*i,300], 5, "white")
        canvas.draw_line([600-110*i,300],[300,0+110*i], 5, "white")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
