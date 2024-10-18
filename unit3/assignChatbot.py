#Micah Kennedy
#10/17/2024
#Pd1-2

import random

# Function to get a random response
def get_random_response():
    responses = [
        "That's so in right now!",
        "Wow, so stylish!",
        "Great choice!",
        "You've got a good eye for fashion!",
        "That's a trendy pick!"
    ]
    return random.choice(responses)
    
# Chatbot introduction
print("Welcome to FashionBot! Let's talk about your style preferences.")

# Get user's name
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Let's dive into fashion.")

# Question 1: Age
age = int(input("How old are you? "))
if age < 18:
    print("You're never too young to develop your own style!")
elif age < 30:
    print("Your twenties are a great time to experiment with fashion!")
else:
    print("Style has no age limit. Keep rocking your look!")

# Question 2: Favorite color
color = input("What's your favorite color to wear? ").lower()
if color == "black":
    print("Black is classic and goes with everything!")
elif color == "white":
    print("White is so fresh and clean!")
else:
    print(f"{color.capitalize()} is a great color to express yourself!")

# Question 3: Shoe preference
shoes = input("What type of shoes do you prefer? ")
print(f"{shoes.capitalize()}? {get_random_response()}")

# Question 4: Top preference
top = input("What's your go-to top style? ")
print(f"I love {top}! They're so versatile.")

# Question 5: Bottom preference
bottom = input("What about your favorite type of bottoms? ")
if "jeans" in bottom.lower():
    print("Jeans are a staple in any wardrobe!")
elif "skirt" in bottom.lower():
    print("Skirts can be both casual and dressy. Great choice!")
else:
    print(f"{bottom.capitalize()} are an excellent pick!")

# Question 6: Accessory preference
accessory = input("What's your favorite accessory? ")
print(f"{accessory.capitalize()} can really complete an outfit. {get_random_response()}")

# Random fashion tip
tips = [
    "Don't be afraid to mix patterns!",
    "Accessories can transform an outfit.",
    "Confidence is the best accessory you can wear!",
    "Experiment with layering for unique looks.",
    "Invest in quality basics for a versatile wardrobe."
]
print("\nHere's a random fashion tip for you:")
print(random.choice(tips))

# Conclusion
print(f"\nThanks for chatting about fashion with me, {name}! Your style sounds amazing.")
