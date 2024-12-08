import simplegui

# Global variable
frame_count = 0

# Colors
sky_blue = "#87CEEB"
grass_green = "#32CD32"
sun_yellow = "#FFD700"
cloud_white = "#FFFFFF"
house_brown = "#8B4513"
roof_red = "#B22222"

def draw_scene(canvas):
    global frame_count
    frame_count += 1
    
    # Sky
    canvas.draw_polygon([(0, 0), (600, 0), (600, 400), (0, 400)], 1, sky_blue, sky_blue)
    
    # Sun
    sun_y = 100 + 20 * abs((frame_count % 120) - 60) / 60
    canvas.draw_circle((50, sun_y), 30, 2, sun_yellow, sun_yellow)
    
    # Grass
    canvas.draw_polygon([(0, 300), (600, 300), (600, 400), (0, 400)], 1, grass_green, grass_green)
    
    # House
    canvas.draw_polygon([(200, 200), (400, 200), (400, 350), (200, 350)], 2, house_brown, house_brown)
    canvas.draw_polygon([(200, 200), (300, 100), (400, 200)], 2, roof_red, roof_red)
    
    # Door
    canvas.draw_polygon([(280, 280), (320, 280), (320, 350), (280, 350)], 2, "black", "brown")
    
    # Window
    canvas.draw_polygon([(220, 230), (260, 230), (260, 270), (220, 270)], 2, "black", "white")
    
    # Clouds
    for i in range(2):
        cloud_x = (frame_count + i * 200) % (600 + 100) - 50
        canvas.draw_circle((cloud_x, 80), 20, 1, cloud_white, cloud_white)
        canvas.draw_circle((cloud_x + 20, 70), 20, 1, cloud_white, cloud_white)
        canvas.draw_circle((cloud_x + 40, 80), 20, 1, cloud_white, cloud_white)
    
    # Tree
    canvas.draw_line((500, 350), (500, 250), 10, "brown")
    for j in range(3):
        canvas.draw_circle((500, 250 - j * 30), 25, 1, "green", "green")
    
    # Birds
    for k in range(5):
        bird_x = (frame_count * 2 + k * 50) % 600
        bird_y = 150 + 10 * abs(((frame_count + k * 20) % 80) - 40) / 40
        canvas.draw_line((bird_x - 10, bird_y), (bird_x, bird_y - 5), 2, "black")
        canvas.draw_line((bird_x, bird_y - 5), (bird_x + 10, bird_y), 2, "black")

frame = simplegui.create_frame("Assigmnent 6: Animation", 600, 400)
frame.set_draw_handler(draw_scene)
frame.start()
