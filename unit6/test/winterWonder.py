import simplegui
import random

# Constants
WIDTH = 800
HEIGHT = 600
DAY_COLOR = "#87CEEB"
NIGHT_COLOR = "#191970"
SNOW_COLOR = "#FFFFFF"
SNOWMEN = "#f5f2f2"
GROUND_COLOR = "#FFFFFF"
TREE_COLOR = "#228B22"
MOON_COLOR = "#FFFACD"
SUN_COLOR = "#FFD700"
HOUSE_COLORS = ["#8B4513", "#A0522D", "#CD853F", "#DEB887"]
TRUNK_COLOR = "#8B4513"

# Global variables
is_day = True
snowflakes = []
trees = []
houses = []
snowmen = []
reindeer = None

# Helper functions
def create_snowflakes(num):
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5)) for _ in range(num)]

def create_trees(num):
    # Modify tree generation to spread them out
    return [(random.randint(50, WIDTH-50), 
             random.randint(HEIGHT//2, HEIGHT-100), 
             random.randint(30, 80)) for _ in range(num)]
    
def create_houses(num_houses, trees):
    houses = []
    attempts = 0
    max_attempts = 100

    while len(houses) < num_houses and attempts < max_attempts:
        # Define house parameters
        size = random.randint(60, 100)
        x = random.randint(50, WIDTH - size - 50)
        y = random.randint(HEIGHT//2, HEIGHT - size - 50)
        color = random.choice(HOUSE_COLORS)

        # Check that house is in front of trees (lower y-coordinate)
        valid_placement = True
        for tree_x, tree_y, tree_size in trees:
            # Check if house is horizontally near a tree
            if abs(x - tree_x) < size + tree_size:
                # Ensure house is in front of the tree
                if y > tree_y:
                    continue
                else:
                    valid_placement = False
                    break

        # Check for overlap with existing houses
        for house_x, house_y, house_size, _ in houses:
            if (abs(x - house_x) < size + house_size and 
                abs(y - house_y) < size + house_size):
                valid_placement = False
                break

        if valid_placement:
            houses.append((x, y, size, color))
        
        attempts += 1

    return houses

def create_snowmen(num):
    return [(random.randint(50, WIDTH-50), random.randint(HEIGHT//2+100, HEIGHT-50)) for _ in range(num)]

def create_reindeer():
    return (random.randint(50, WIDTH-100), random.randint(HEIGHT//2+50, HEIGHT-100))

# Event handlers
def toggle_day_night():
    global is_day
    is_day = not is_day

def draw_snowflake(canvas, x, y, size):
    canvas.draw_circle((x, y), size, 1, SNOW_COLOR, SNOW_COLOR)

def draw_tree(canvas, x, y, size):
    canvas.draw_polygon([(x, y), (x - size//2, y + size), (x + size//2, y + size)], 1, TREE_COLOR, TREE_COLOR)
    # Draw the trunk of the tree (rectangle)
    trunk_width = size // 5
    trunk_height = size // 3
    trunk_x = x - trunk_width // 2
    trunk_y = y + size
    
    canvas.draw_polygon([(trunk_x,trunk_y),(trunk_x + trunk_width,trunk_y),
                         (trunk_x + trunk_width,trunk_y + trunk_height),
                         (trunk_x,trunk_y + trunk_height)], 
                        1 ,TRUNK_COLOR ,TRUNK_COLOR)

def draw_sun_moon(canvas):
    if is_day:
        canvas.draw_circle((WIDTH - 100, 100), 50, 1, SUN_COLOR, SUN_COLOR)
    else:
        canvas.draw_circle((100, 100), 40, 1, MOON_COLOR, MOON_COLOR)

def draw_house(canvas, x, y, size, color):
    # House body
    canvas.draw_polygon([(x, y), (x + size, y), (x + size, y + size), (x, y + size)], 1, color, color)
    # Roof
    canvas.draw_polygon([(x, y), (x + size//2, y - size//2), (x + size, y)], 1, "#8B4513", "#8B4513")
    # Window
    window_size = size // 4
    window_x = x + size // 4
    window_y = y + size // 4
    canvas.draw_polygon([(window_x, window_y), (window_x + window_size, window_y), 
                         (window_x + window_size, window_y + window_size), (window_x, window_y + window_size)], 
                        1, "yellow" if is_day else "#FFD700", "yellow" if is_day else "#FFD700")
    # Door
    door_width = size // 3
    door_height = size // 2
    door_x = x + (size - door_width) // 2
    door_y = y + size - door_height
    canvas.draw_polygon([(door_x, door_y), (door_x + door_width, door_y), 
                         (door_x + door_width, y + size), (door_x, y + size)], 
                        1, "#8B4513", "#8B4513")

def draw_snowman(canvas, x, y):
    # Bottom snowball
    canvas.draw_circle((x, y), 30, 1, SNOWMEN, SNOWMEN)
    # Middle snowball
    canvas.draw_circle((x, y-50), 20, 1, SNOWMEN, SNOWMEN)
    # Head
    canvas.draw_circle((x, y-85), 15, 1, SNOWMEN, SNOWMEN)
    # Eyes
    canvas.draw_circle((x-7, y-90), 2, 1, "Black", "Black")
    canvas.draw_circle((x+7, y-90), 2, 1, "Black", "Black")
    # Carrot nose
    canvas.draw_polygon([(x, y-85), (x+15, y-85), (x, y-80)], 1, "Orange", "Orange")
    # Buttons
    canvas.draw_circle((x, y-50), 2, 1, "Black", "Black")
    canvas.draw_circle((x, y-30), 2, 1, "Black", "Black")
    canvas.draw_circle((x, y-10), 2, 1, "Black", "Black")

def draw_reindeer(canvas, x, y):
    # Body
    canvas.draw_line((x, y), (x+60, y), 20, "Brown")
    # Legs
    canvas.draw_line((x+10, y), (x+10, y+40), 5, "Brown")
    canvas.draw_line((x+50, y), (x+50, y+40), 5, "Brown")
    # Neck
    canvas.draw_line((x+60, y), (x+80, y-30), 10, "Brown")
    # Head
    canvas.draw_circle((x+85, y-40), 15, 1, "Brown", "Brown")
    # Eye
    canvas.draw_circle((x+90, y-45), 2, 1, "Black", "Black")
    # Antlers
    canvas.draw_polyline([(x+85, y-55), (x+95, y-70), (x+105, y-60)], 2, "Brown")
    canvas.draw_polyline([(x+85, y-55), (x+75, y-70), (x+65, y-60)], 2, "Brown")
    
def draw(canvas):
    # Background
    canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, DAY_COLOR if is_day else NIGHT_COLOR, DAY_COLOR if is_day else NIGHT_COLOR)
    
    # Ground
    canvas.draw_polygon([(0, HEIGHT//2), (WIDTH, HEIGHT//2), (WIDTH, HEIGHT), (0, HEIGHT)], 1, GROUND_COLOR, GROUND_COLOR)
    
    # Trees
    for x, y, size in trees:
        draw_tree(canvas, x, y, size)
    
    # Houses
    for x, y, size, color in houses:
        draw_house(canvas, x, y, size, color)
    
    # Snowmen
    for x, y in snowmen:
        draw_snowman(canvas, x, y)
    
    # Reindeer
    if reindeer:
        draw_reindeer(canvas, reindeer[0], reindeer[1])
    
    # Sun/Moon
    draw_sun_moon(canvas)
    
    # Snowflakes
    for i, (x, y, size) in enumerate(snowflakes):
        draw_snowflake(canvas, x, y, size)
        snowflakes[i] = (x, (y + 1) % HEIGHT, size)

# Create frame
frame = simplegui.create_frame("Winter Wonderland", WIDTH, HEIGHT)

# Register event handlers
frame.set_draw_handler(draw)
frame.add_button("Toggle Day/Night", toggle_day_night, 200)

# Initialize scene elements
snowflakes = create_snowflakes(100)
trees = create_trees(10)
houses = create_houses(5, trees)
snowmen = create_snowmen(2)
reindeer = create_reindeer()

# Start frame
frame.start()
