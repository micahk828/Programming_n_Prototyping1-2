#Micah Kennedy
#Pd 1-2
#11/29/2024

import simplegui

# Colors
brown = "#8B4513"
orange = "#FFA500"
red = "#FF0000"
yellow = "#FFD700"
green = "#228B22"

def draw_handler(canvas):
     # Background
    canvas.draw_polygon([(0, 0), (600, 0), (600, 400), (0, 400)], 1, "#87CEEB", "#87CEEB") 
    
    # Ground
    canvas.draw_polygon([(0, 300), (600, 300), (600, 400), (0, 400)], 1, green, green) 
    
    # Turkey body
    canvas.draw_circle((300, 250), 50, 2, brown, brown)
    # Turkey head
    canvas.draw_circle((260, 220), 20, 2, brown, brown)
    # Turkey beak
    canvas.draw_polygon([(219, 220), (239, 215), (239, 225)], 1, orange, orange)
    # Turkey eye
    canvas.draw_circle((255, 215), 5, 1, "black", "black")
    # Turkey feet
    canvas.draw_line((290, 300), (270, 320), 3, orange)
    canvas.draw_line((310, 300), (330, 320), 3, orange)
    # Tail feathers
    colors = [red, orange, yellow]
    for i in range(5):
        canvas.draw_line((350, 250), (390, 210 + i * 20), 5, colors[i % 3])
    
    # Pumpkin 1
    canvas.draw_circle((100, 330), 30, 2, orange, orange)
    canvas.draw_line((100, 300), (100, 280), 3, green)
    # Pumpkin 2
    canvas.draw_circle((500, 330), 40, 2, orange, orange)
    canvas.draw_line((500, 290), (500, 270), 3, green)


frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
