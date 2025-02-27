#Micah Kennedy
#Pd 1-2
#Challenge 2

def right_justify(s):
    num_spaces = 70 - len(s)  # Calculate the number of spaces needed
    print(" " * num_spaces + s)  # Print spaces followed by the string
s = input("What is your word: ") # Ask user for their word
right_justify(s) #calls function with inputed word as parameter
