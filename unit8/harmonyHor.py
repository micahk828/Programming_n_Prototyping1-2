import simplegui
import random

current_room = "Resource Center"
inventory = []
health = 100
score = 0
player_pos = [200, 300]  # Starting position of the player
game_state = "playing"  
quest_stage = 0  
move_direction = None
move_count = 0

rooms = {
    "Resource Center": {
        "description": "A bustling hub of supplies. You can gather resources here.",
        "north": "Conflict Zone",
        "items": ["Water", "Food"],
        "color": "LightGreen",
        "border": "Green"
    },
    "Conflict Zone": {
        "description": "Tensions are high here. Choose your actions wisely to maintain peace.",
        "south": "Resource Center",
        "east": "Trade Post",
        "items": ["Medicine"],
        "color": "LightCoral",
        "border": "Red"
    },
    "Trade Post": {
        "description": "Traders exchange goods and information. A great place to barter.",
        "west": "Conflict Zone",
        "items": ["Tools"],
        "color": "LightBlue",
        "border": "Blue"
    }
}

# Quests
quests = [
    "Collect water and food from the Resource Center",
    "Resolve a conflict in the Conflict Zone",
    "Trade for tools at the Trade Post",
    "Return to the Resource Center with all items"
]


def update_gui():
    room_label.set_text(f"Room: {current_room}")
    description_label.set_text(rooms[current_room]["description"])
    inventory_label.set_text(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    health_label.set_text(f"Health: {health}")
    score_label.set_text(f"Score: {score}")
    quest_label.set_text(f"Current Quest: {quests[quest_stage]}")

def draw(canvas):
    if game_state == "playing":
        canvas.draw_polygon([(0, 0), (400, 0), (400, 400), (0, 400)], 1, 
                            rooms[current_room]["border"], 
                            rooms[current_room]["color"])

        if current_room == "Resource Center":
            canvas.draw_circle((100, 100), 30, 2, "Brown", "Green")  # Tree
            canvas.draw_polygon([(300, 200), (350, 250), (250, 250)], 2, "Gray", "Gray")  # Mountain
        elif current_room == "Conflict Zone":
            canvas.draw_line((100, 100), (300, 300), 2, "Black")  # Conflict line
            canvas.draw_line((300, 100), (100, 300), 2, "Black")  # Conflict line
        elif current_room == "Trade Post":
            canvas.draw_polygon([(150, 200), (250, 200), (200, 150)], 2, "Brown", "Brown")  # Tent
            canvas.draw_circle((300, 100), 20, 2, "Yellow", "Gold")  # Gold coin

        canvas.draw_circle(player_pos, 20, 2, "Black", "Yellow")
        canvas.draw_text("Player", (player_pos[0] - 20, player_pos[1] + 40), 16, "Black")

        canvas.draw_text(f"Room: {current_room}", (10, 20), 18, "White")
        canvas.draw_text(f"Health: {health}", (10, 40), 18, "White")
        canvas.draw_text(f"Score: {score}", (10, 60), 18, "White")
    
    elif game_state == "won":
        canvas.draw_polygon([(0, 0), (400, 0), (400, 400), (0, 400)], 1, "Gold", "LightYellow")
        canvas.draw_text("Congratulations!", (100, 150), 36, "Green")
        canvas.draw_text("You've won the game!", (80, 200), 24, "Green")
        canvas.draw_text(f"Final Score: {score}", (150, 250), 20, "Black")
    
    elif game_state == "lost":
        canvas.draw_polygon([(0, 0), (400, 0), (400, 400), (0, 400)], 1, "Red", "Pink")
        canvas.draw_text("Game Over!", (130, 150), 36, "Red")
        canvas.draw_text("You've run out of health.", (80, 200), 24, "Red")
        canvas.draw_text(f"Final Score: {score}", (150, 250), 20, "Black")

def go_north():
    go("north")
    check_quest_progress()
    check_game_over()

def go_south():
    go("south")
    check_quest_progress()
    check_game_over()

def go_east():
    go("east")
    check_quest_progress()
    check_game_over()

def go_west():
    go("west")
    check_quest_progress()
    check_game_over()
        
        
def move_player():
    global player_pos, move_direction, move_count
    if move_direction:
        if move_direction == "north" and player_pos[1] > 50:
            player_pos[1] -= 5
        elif move_direction == "south" and player_pos[1] < 350:
            player_pos[1] += 5
        elif move_direction == "east" and player_pos[0] < 350:
            player_pos[0] += 5
        elif move_direction == "west" and player_pos[0] > 50:
            player_pos[0] -= 5
        
        move_count += 1
        if move_count >= 50:  
            move_direction = None
            move_count = 0

def go(direction):
    global current_room, move_direction
    if game_state == "playing":
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            move_direction = direction
            random_event()  
            update_gui()
        else:
            feedback_label.set_text("You can't go that way!")

def pick_up_item():
    global score, game_state, quest_stage
    if game_state == "playing":
        if rooms[current_room]["items"]:
            item = rooms[current_room]["items"].pop(0)  
            inventory.append(item)
            score += 10  
            feedback_label.set_text(f"You picked up: {item}")
            update_gui()
            check_quest_progress()
        else:
            feedback_label.set_text("No items to pick up here.")

def random_event():
    global health
    event_outcome = random.randint(1, 3)
    if event_outcome == 1:
        health -= 10
        feedback_label.set_text("A small conflict erupted! You lost 10 health.")
    elif event_outcome == 2:
        feedback_label.set_text("You found some extra supplies. All is calm.")
    else:
        health += 5
        feedback_label.set_text("You resolved a dispute peacefully! Gained 5 health.")
    check_game_over()

def check_game_over():
    global health, game_state
    if health <= 0:
        game_state = "lost"
        feedback_label.set_text("Game Over! You ran out of health.")

def check_quest_progress():
    global quest_stage, game_state
    if quest_stage == 0 and "Water" in inventory and "Food" in inventory:
        quest_stage = 1
        feedback_label.set_text("Quest complete! Head to the Conflict Zone.")
    elif quest_stage == 1 and current_room == "Conflict Zone" and health > 80:
        quest_stage = 2
        feedback_label.set_text("Conflict resolved! Proceed to the Trade Post.")
    elif quest_stage == 2 and "Tools" in inventory:
        quest_stage = 3
        feedback_label.set_text("Tools acquired! Return to the Resource Center.")
    elif quest_stage == 3 and current_room == "Resource Center" and len(inventory) == 4:
        game_state = "won"
        feedback_label.set_text("Congratulations! You've completed all quests and won the game!")
    update_gui()


frame = simplegui.create_frame("Harmony Horizon", 400, 400)

room_label = frame.add_label("Room: Resource Center")
description_label = frame.add_label("Description: A bustling hub of supplies.")
inventory_label = frame.add_label("Inventory: Empty")
health_label = frame.add_label("Health: 100")
score_label = frame.add_label("Score: 0")
quest_label = frame.add_label("Current Quest: Collect water and food from the Resource Center")
feedback_label = frame.add_label("Welcome to Harmony Horizon! Explore and keep the peace.")

frame.add_button("Up", go_north, 100)
frame.add_button("Down", go_south, 100)
frame.add_button("Right", go_east, 100)
frame.add_button("Left", go_west, 100)
frame.add_button("Take Object", pick_up_item, 100)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(50, move_player)
timer.start()

update_gui()
frame.start()
