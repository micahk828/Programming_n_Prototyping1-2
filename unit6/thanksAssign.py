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
sky_blue = "#87CEEB"
black = "black"
white = "#FFFFFF"
sunflower_yellow = "#FFD700"

# Constants for canvas size
canvas_width = 600
canvas_height = 400

def draw_handler(canvas):
    # Draw background sky
    draw_background(canvas)
    
    # Draw ground
    draw_ground(canvas)
    
    # Draw sunflowers in the corners
    draw_sunflower(canvas, 50, 50)  # Top left corner
    draw_sunflower(canvas, canvas_width - 50, 50)  # Top right corner
    
    # Draw turkey
    draw_turkey(canvas, 300, 250)
    
    # Draw pumpkins
    draw_pumpkin(canvas, 100, 330, 30)
    draw_pumpkin(canvas, 500, 330, 40)
    
    #Draw Pilgrim Hat
    draw_pilgrim_hat(canvas, 260, 180)

def draw_background(canvas):
    canvas.draw_polygon([(0, 0), (canvas_width, 0), (canvas_width, canvas_height), (0, canvas_height)], 1, sky_blue, sky_blue)

def draw_ground(canvas):
    canvas.draw_polygon([(0, canvas_height - 100), (canvas_width, canvas_height - 100), (canvas_width, canvas_height), (0, canvas_height)], 1, green, green)

def draw_turkey(canvas, x_center, y_center):
    # Body
    canvas.draw_circle((x_center, y_center), 50, 2, brown, brown)
    # Head
    canvas.draw_circle((x_center - 40, y_center - 30), 20, 2, brown, brown)
    # Beak
    canvas.draw_polygon([(x_center - 79, y_center - 30), (x_center - 59, y_center - 35), (x_center - 59, y_center - 25)], 1, orange, orange)
    # Eye
    canvas.draw_circle((x_center - 45, y_center - 35), 5, 1, black, black)
    # Feet
    canvas.draw_line((x_center - 10, y_center + 50), (x_center - 30, y_center + 70), 3, orange)
    canvas.draw_line((x_center + 10, y_center + 50), (x_center + 30, y_center + 70), 3, orange)
    
    # Tail feathers
    colors = [red, orange, yellow]
    for i in range(5):
        canvas.draw_line((350, 250), (390, 210 + i * 20), 5, colors[i % 3])


def draw_pumpkin(canvas, x_center, y_bottom, radius):
    # Pumpkin body
    canvas.draw_circle((x_center , y_bottom ), radius ,2 , orange , orange )
    # Pumpkin stem
    canvas.draw_line((x_center , y_bottom - radius ), (x_center , y_bottom - radius -20 ), int(radius/10) , green)

def draw_pilgrim_hat(canvas, x_center, y_top):
    # Hat brim
    brim_width = 120
    brim_height = 20
    # Draw brim of the hat
    canvas.draw_polygon([(x_center - brim_width // 2 , y_top), (x_center + brim_width // 2 , y_top), (x_center + brim_width // 2 , y_top + brim_height), (x_center - brim_width // 2 , y_top + brim_height)], 1, black, black)
    # Hat top
    hat_height = 80
    # Draw top of the hat
    canvas.draw_polygon([(x_center - brim_width // 4 , y_top), (x_center + brim_width // 4 , y_top), (x_center + brim_width // 4 , y_top - hat_height), (x_center - brim_width // 4 , y_top - hat_height)], 1, black, black)
    # Hat buckle
    buckle_width = brim_width // 5
    buckle_height = brim_height // 2
    # Draw buckle of the hat
    canvas.draw_polygon([(x_center - buckle_width // 2 , y_top + brim_height // 2), (x_center + buckle_width // 2 , y_top + brim_height // 2), (x_center + buckle_width // 2 , y_top + brim_height // 2 + buckle_height), (x_center - buckle_width // 2 , y_top + brim_height // 2 + buckle_height)], 1, white, white)

def draw_sunflower(canvas, x_center, y_center):
    petal_length = 30
    center_radius = 15
    # Draw petals
    canvas.draw_line((x_center - petal_length, y_center), (x_center + petal_length, y_center), 10, sunflower_yellow)
    canvas.draw_line((x_center, y_center - petal_length), (x_center, y_center + petal_length), 10, sunflower_yellow)
    canvas.draw_line((x_center - petal_length, y_center - petal_length), (x_center + petal_length, y_center + petal_length), 5, sunflower_yellow)
    canvas.draw_line((x_center - petal_length, y_center + petal_length), (x_center + petal_length, y_center - petal_length), 5, sunflower_yellow)
    # Draw center of sunflower
    canvas.draw_circle((x_center, y_center), center_radius, 1, brown, brown)
    # Draw dotted circle around sunflower using draw_point
    circle_radius = petal_length + 10
    for i in range(16):
        canvas.draw_point((x_center + circle_radius, y_center + i * 5 - 40), black)
        canvas.draw_point((x_center - circle_radius, y_center + i * 5 - 40), black)
        canvas.draw_point((x_center + i * 5 - 40, y_center + circle_radius), black)
        canvas.draw_point((x_center + i * 5 - 40, y_center - circle_radius), black)

# Create frame and set handlers
frame = simplegui.create_frame("Thanksgiving Drawing", canvas_width , canvas_height)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)

# Start frame
frame.start()
