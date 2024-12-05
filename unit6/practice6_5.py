import simplegui
import math

def draw_house(canvas):
    # Draw house box
    canvas.draw_polygon([(200, 300), (400, 300), (400, 500), (200, 500)], 2, "Brown", "Tan")
    
    # Draw roof
    canvas.draw_polygon([(200, 300), (300, 200), (400, 300)], 2, "Brown", "Red")
    
    # Draw door
    canvas.draw_polygon([(270, 400), (330, 400), (330, 500), (270, 500)], 2, "Brown", "SaddleBrown")
    canvas.draw_polygon([(317, 447), (323, 447), (323, 453), (317, 453)], 2, "Yellow", "Yellow")  # Doorknob
    
    # Draw windows
    canvas.draw_polygon([(220, 350), (260, 350), (260, 390), (220, 390)], 2, "White", "LightBlue")
    canvas.draw_polygon([(340, 350), (380, 350), (380, 390), (340, 390)], 2, "White", "LightBlue")

def draw_tree(canvas, x, y):
    # Draw trunk
    canvas.draw_line((x, y), (x, y - 100), 20, "Brown")
    
    # Draw leaves
    canvas.draw_circle((x, y - 130), 50, 2, "Green", "Green")


def draw_cloud(canvas, x, y):
    canvas.draw_circle((x, y), 20, 1, "White", "White")
    canvas.draw_circle((x + 15, y - 10), 20, 1, "White", "White")
    canvas.draw_circle((x + 30, y), 20, 1, "White", "White")
    canvas.draw_circle((x + 15, y + 10), 20, 1, "White", "White")

def draw_handler(canvas):
    # Draw sky
    canvas.draw_polygon([(0, 0), (600, 0), (600, 400), (0, 400)], 1, "SkyBlue", "SkyBlue")
    
    # Draw ground
    canvas.draw_polygon([(0, 400), (600, 400), (600, 600), (0, 600)], 1, "Green", "Green")
    
    # Draw house
    draw_house(canvas)
    
    # Draw trees
    draw_tree(canvas, 100, 500)
    draw_tree(canvas, 500, 500)
    
    
    # Draw clouds
    draw_cloud(canvas, 150, 100)
    draw_cloud(canvas, 400, 150)

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
