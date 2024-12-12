import simplegui
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
DAY_COLOR = "#87CEEB"
NIGHT_COLOR = "#191970"
TRANSITION_DURATION = 5  # seconds
SNOW_COLOR = "#FFFFFF"
GROUND_COLOR = "#FFFFFF"
TREE_COLOR = "#228B22"
TRUNK_COLOR = "#8B4513"
MOON_COLOR = "#FFFACD"
SUN_COLOR = "#FFD700"
HOUSE_COLORS = ["#8B4513", "#A0522D", "#CD853F", "#DEB887"]

# Global variables
time_of_day = 0  # 0 to 1, where 0 is day and 1 is night
snowflakes = []
trees = []
houses = []
snowmen = []
reindeer = None

# Helper functions

def create_snowflakes(num):
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5)) for _ in range(num)]

def create_trees(num):
    return [(random.randint(50, WIDTH-50), random.randint(HEIGHT//2, HEIGHT-100), random.randint(30, 80)) for _ in range(num)]

def create_houses(num_houses, trees):
    houses = []
    attempts = 0
    max_attempts = 100

    while len(houses) < num_houses and attempts < max_attempts:
        size = random.randint(60, 100)
        x = random.randint(50, WIDTH - size - 50)
        y = random.randint(HEIGHT//2, HEIGHT - size - 50)
        color = random.choice(HOUSE_COLORS)

        valid_placement = True
        for tree_x, tree_y, tree_size in trees:
            if abs(x - tree_x) < size + tree_size:
                if y > tree_y:
                    continue
                else:
                    valid_placement = False
                    break

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
    return [(random.randint(50, WIDTH-50), random.randint(HEIGHT//2+100, HEIGHT-50), random.choice([-1, 1])) for _ in range(num)]

def create_reindeer():
    return (random.randint(50, WIDTH), HEIGHT // 2 + 20)

def update_time_of_day(canvas):
    global time_of_day
    time_of_day = (time_of_day + 1 / (60 * TRANSITION_DURATION)) % 1

def interpolate_color(color1, color2, t):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"

def draw_snowflake(canvas, x, y, size):
    canvas.draw_circle((x, y), size, 1, SNOW_COLOR, SNOW_COLOR)

def draw_tree(canvas, x, y, size):
    # Draw the tree top (triangle)
    canvas.draw_polygon([(x,y),(x-size//2,y+size),(x+size//2,y+size)], 1,TREE_COLOR,TREE_COLOR)
    
    # Draw the trunk of the tree (rectangle)
    trunk_width = size // 5
    trunk_height = size // 3
    trunk_x = x - trunk_width // 2
    trunk_y = y + size
    
    canvas.draw_polygon([(trunk_x,trunk_y),(trunk_x + trunk_width,trunk_y),
                         (trunk_x + trunk_width,trunk_y + trunk_height),
                         (trunk_x,trunk_y + trunk_height)], 
                        1 ,TRUNK_COLOR ,TRUNK_COLOR)

def draw_house(canvas,x,y,size,color):
     # House body
    canvas.draw_polygon([(x,y),(x+size,y),(x+size,y+size),(x,y+size)], 1,color,color)
     # Roof
    canvas.draw_polygon([(x,y),(x+size//2,y-size//2),(x+size,y)], 1,"#8B4513","#8B4513")
     # Window
    window_size=size//4
    window_x=x+size//4
    window_y=y+size//4
    canvas.draw_polygon([(window_x,window_y),(window_x+window_size,window_y),
                          (window_x+window_size,window_y+window_size),(window_x,window_y+window_size)],
                         1,"yellow" if time_of_day<0.5 else "#FFD700","yellow" if time_of_day<0.5 else "#FFD700")
      # Door 
    door_width=size//3 
    door_height=size//2 
    door_x=x+(size-door_width)//2 
    door_y=y+size-door_height 
    canvas.draw_polygon([(door_x ,door_y),(door_x +door_width ,door_y),
                           (door_x +door_width ,y +size),(door_x ,y +size)],
                          1 ,TRUNK_COLOR ,TRUNK_COLOR)

def draw_snowman(canvas,x,y,direction):
    global snowmen 
    
    new_x=x+direction*2 
    
    valid_move=True 
    
    for tree_x ,tree_y ,tree_size in trees: 
        if abs(new_x-tree_x)<30+tree_size: 
            valid_move=False 
            break 
        
    for house_x ,house_y ,house_size,_ in houses: 
        if abs(new_x-house_x)<30+house_size: 
            valid_move=False 
            break 
        
        if valid_move: 
            x=new_x 
            if x<50 or x>WIDTH-50: 
                direction+=-1 
        
    #snowmen[snowmen.index((x,y,direction))]=(x,y,direction) 

    canvas.draw_circle((x,y),30 ,1 ,SNOW_COLOR ,SNOW_COLOR) 
    canvas.draw_circle((x,y-50),20 ,1 ,SNOW_COLOR ,SNOW_COLOR) 
    canvas.draw_circle((x,y-85),15 ,1 ,SNOW_COLOR ,SNOW_COLOR) 
    canvas.draw_circle((x-7,y-90),2 ,1 ,"Black","Black") 
    canvas.draw_circle((x+7,y-90),2 ,1 ,"Black","Black") 
    canvas.draw_polygon([(x,y-85),(x+15,y-85),(x,y-80)],1,"Orange","Orange") 
    canvas.draw_circle((x,y-50),2 ,1 ,"Black","Black") 
    canvas.draw_circle((x,y-30),2 ,1 ,"Black","Black") 
    canvas.draw_circle((x,y-10),2 ,1 ,"Black","Black")

def draw_reindeer(canvas,x,y):
    global reindeer 
    
    new_x=x+2 
    
    if new_x>WIDTH or new_x<0: 
        new_x=0 
    
    reindeer=(new_x,y) 
    
    canvas.draw_line((new_x,y),(new_x+60,y),20,"Brown") 
    canvas.draw_line((new_x+10,y),(new_x+10,y+40),5,"Brown") 
    canvas.draw_line((new_x+50,y),(new_x+50,y+40),5,"Brown") 
    canvas.draw_line((new_x+60,y),(new_x+80,y-30),10,"Brown") 
    canvas.draw_circle((new_x+85,y-40),15 ,1 ,"Brown","Brown") 
    canvas.draw_circle((new_x+90,y-45),2 ,1 ,"Black","Black") 
    canvas.draw_polyline([(new_x+85,y-55),(new_x+95,y-70),(new_x+105,y-60)],2,"Brown") 
    canvas.draw_polyline([(new_x+85,y-55),(new_x+75,y-70),(new_x+65,y-60)],2,"Brown")

def draw_sun_moon(canvas): 
    sun_moon_x=WIDTH-100+200*math.sin(time_of_day*math.pi) 
    sun_moon_y=100+50*math.sin(time_of_day*math.pi) 
    sun_moon_color=interpolate_color(SUN_COLOR,MOON_COLOR,time_of_day) 
    canvas.draw_circle((sun_moon_x,sun_moon_y),40 ,1 ,sun_moon_color,sun_moon_color)

def draw(canvas): 
    global time_of_day 
    
    update_time_of_day(canvas) 
    
    sky_color=interpolate_color(DAY_COLOR,NIGHT_COLOR,time_of_day) 
    
    canvas.draw_polygon([(0 ,0),(WIDTH ,0),(WIDTH ,HEIGHT),(0 ,HEIGHT)], 
                          1 ,sky_color ,sky_color) 
    
    ground_color=GROUND_COLOR 
    
    canvas.draw_polygon([(0 ,HEIGHT//2),(WIDTH ,HEIGHT//2),(WIDTH ,HEIGHT),(0 ,HEIGHT)], 
                            1 ,ground_color ,ground_color) 
    
    for x,y,size in trees: 
        draw_tree(canvas,x,y,size) 
    
    for x,y,size,color in houses: 
        draw_house(canvas,x,y,size,color) 
    
    for x,y,direction in snowmen: 
        draw_snowman(canvas,x,y,direction) 
    
    if reindeer: 
        draw_reindeer(canvas,reindeer[0],reindeer[1]) 
    
    draw_sun_moon(canvas) 
    
    for i,(x,y,size) in enumerate(snowflakes): 
        draw_snowflake(canvas,x,y,size) 
        snowflakes[i]=(x,(y +1)%HEIGHT,size)

# Create frame and initialize scene elements frame=simplegui.create_frame("Winter Wonderland",WIDTH ,HEIGHT)
frame = simplegui.create_frame("Winter Wonderland", WIDTH, HEIGHT)

# Register event handlers
frame.set_draw_handler(draw)

trees=create_trees(10)
houses=create_houses(5,trees)
snowflakes=create_snowflakes(100)
snowmen=create_snowmen(2)
reindeer=create_reindeer()

frame.set_draw_handler(draw)
frame.start()
