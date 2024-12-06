import simplegui

def draw(canvas):
    # Draw face (circle)
    canvas.draw_circle((width // 2, height // 2), radius, 10, "Black", "Yellow")

    # Draw open eye (right)
    canvas.draw_circle((width // 2 + eye_offset_x, height // 2 - eye_offset_y), eye_radius, 1, "Black", "White")
    canvas.draw_circle((width // 2 + eye_offset_x, height // 2 - eye_offset_y), pupil_radius, 1, "Black", "Black")

    # Draw winking eye (left)
    wink_y = height // 2 - eye_offset_y
    wink_left = width // 2 - eye_offset_x - eye_radius
    wink_right = width // 2 - eye_offset_x + eye_radius
    canvas.draw_line((wink_left, wink_y), (wink_right, wink_y), 3, "Black")

    # Draw smile (using multiple lines)
    smile_center_x = width // 2
    smile_center_y = height // 2 + mouth_offset_y
    smile_width = mouth_width
    smile_height = mouth_height

    # Draw the smile using 5 connected lines
    canvas.draw_line((smile_center_x - smile_width//2, smile_center_y), 
                     (smile_center_x - smile_width//4, smile_center_y + smile_height//2), 2, "Black")
    canvas.draw_line((smile_center_x - smile_width//4, smile_center_y + smile_height//2),
                     (smile_center_x, smile_center_y + smile_height), 2, "Black")
    canvas.draw_line((smile_center_x, smile_center_y + smile_height),
                     (smile_center_x + smile_width//4, smile_center_y + smile_height//2), 2, "Black")
    canvas.draw_line((smile_center_x + smile_width//4, smile_center_y + smile_height//2),
                     (smile_center_x + smile_width//2, smile_center_y), 2, "Black")

def set_dimensions():
    global width, height, radius, eye_radius, pupil_radius
    global eye_offset_x, eye_offset_y, mouth_width, mouth_height, mouth_offset_y

    width = int(input("Enter width of the emoji: "))
    height = int(input("Enter height of the emoji: "))
    
    # Set parameters relative to dimensions
    radius = min(width, height) // 3
    eye_radius = radius // 6
    pupil_radius = radius // 12
    eye_offset_x = radius // 2
    eye_offset_y = radius // 3
    mouth_width = radius * 1.2
    mouth_height = radius * 0.4
    mouth_offset_y = radius // 3

# Main execution starts here
set_dimensions()

# Create a frame
frame = simplegui.create_frame("Winking Emoji Drawer", width, height)

# Register the draw handler
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
