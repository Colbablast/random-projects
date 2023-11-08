# Escape Room!
# Dec 17, 2021
# Colby Campbell

# It's an escape room, meaning the goal is to find a way out! The cool thing about this program isn't about
# the actual the escape room, but the way it can be customized. All of the rooms and items are loaded in from
# a .txt file that can be customized so you can make this adventure as long or short you want! Currently,
# I have created a small demo for this that isn't very difficult but it will show you what this program can do!

# All the needed imports
import sys
from os import system, name
from time import sleep

# CLASSES!
# We are creating the classes for the items and rooms that will be added in from the .txt file
class Item:

  def __init__(self, description, pickup, clue, answer, inside, locked):
    self.description = description
    self.pickup = pickup
    self.clue = clue
    self.answer = answer
    self.inside = inside
    self.locked = locked


class Room:

  def __init__(self, description, adjacent, items, clue, answer, locked):
    self.description = description
    self.adjacent = adjacent
    self.items = items
    self.clue = clue
    self.answer = answer
    self.locked = locked




# VARIABLES!
# What text file the program reads
file_name = "example.txt"

# wait is the time that is waited between each printing each letter on the screen
wait = 0.03

# the text variable dictates whether the player is going to have scrolling text or regular text
text = "print"

# We are adding the variables for the one time things that don't need their own class
introduction = ""
start_room = ""
end_room = ""

# Dictionaries that contain all of the room and item class variables that are created
rooms = {}
items = {}

# Contains all of the items that the player has in their inventory
inventory = []

# Other variable that I cannot find the words to describe what it does
var = ""

# Holds all of the information to make a class as the program iterates through the lines
class_placeholder = []




# FUNCTIONS!
def commands(num):
  print2("Type the name of an", colour(34, "item"), "to look at the item")
  print2("Type the name of a", colour(31, "room"), "to move to that room.")
  print2(colour(num, "Help, commands"), "- Brings this information up.")
  print2(colour(num, "Inventory"), "- Checks your players inventory.")
  print2(colour(num, "Inspect, open, unlock, look at, clue"), "- Get the clue for the item you are looking at.")
  print2(colour(num, "Pickup, take, acquire, yoink, grab"), "- Take the item being looked at.")


# Thanks to: https://www.geeksforgeeks.org/clear-screen-python/
# Just uses the windows or linux system clear to clear the text on the screen
def clear():
    # for windows
    if name == 'nt':
       system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


# Thanks for explaining: https://stackabuse.com/how-to-print-colored-text-in-python/
# Black - 30 \ Red - 31 \ Green - 32 \ Yellow - 33 \ Blue - 34 \ Purple - 35 \ Cyan - 36 \ White - 37
def colour(colour, text):
  # Just combines the text with the needed text to make it a different colour, and returns it
  return "\033[1;" + str(colour) + "m" + text + "\033[0;0m"

def scroll(text):
  # Check if the text has any coloured words (jank code but it works)
  if "\033" in text:
    # Adding ten to the index value to account for the entire colour code stuff
    start = (text.find("\033[1;"), text.find("\033[1;") + 6)
    # Adding 9 for the same reason
    end = (text.find("\033[0;0m"), text.find("\033[0;0m") + 5)
  else:
    start = None

  # Print the word letter by letter, sleeping between every letter (that isn't invisible)
  for index, letter in enumerate(text):
    sys.stdout.write(letter)
    sys.stdout.flush()
    # This is just to get rid of the pause for when it is reading the colour word characters that are invis
    if start is not None:
      if index in range(start[0], start[1] + 1) or index in range(end[0], end[1] + 1):
        continue
    # if the text gets through the above if statements, it sleeps betweeen the characters
    sleep(wait)

  # Makes it so the text isn't all on one line
  print()
  # Pause at the end of each line for a bit to make it look better
  sleep(0.3)


def print2(*input):
  # Joins all of the inputs together so it can print it like a regular print statement
  txt = " ".join(input)
  
  # Use the scroll() function to scroll the text
  if text == "scroll":
    scroll(txt)
  
  # Use the normal print() function to just print the text normally
  else:
    print(txt)


# Check the players inventory
def is_inventory(player_input):
  if "inventory" in player_input:
      if len(inventory) == 0:
        print2("You have nothing in your inventory.")
      else:
        print2("You have:", colour(34, (", ".join(inventory).title())))


def help(player_input, num):
  if "help" in player_input or "commands" in player_input:
    commands(num)


def print_room_info(room_name):
  room_info = rooms.get(current_room.lower())
  # Clear the screen, print the room name, description, adjacent rooms, and items in room
  clear()
  print2(colour(35, room_name.title()))
  print2(room_info.description)
  print2("The adjacent rooms are:", colour(31, ", ".join(room_info.adjacent).title()))
  print2("The items in the room are:", colour(34, ", ".join(room_info.items).title()))


def print_item_info(item_name):
  item_info = items.get(item_name)
  # Clears the screen and prints the item details
  clear()
  print2(colour(34, item_name.title()))
  print2(item_info.description)
  print2("Type \"back\" to go back.")


def player_input(cursor_colour):
  # The place the player inputs da stuff
  choice = input(colour(cursor_colour, "> ")).lower()
  room_info = rooms.get(current_room.lower())

  # Check inventory
  is_inventory(choice)

  # Check if player needs help
  help(choice, 35)

  # Code that finds the room you say in your input
  found_room = ""
  for index, room in enumerate(room_info.adjacent):
    if room.lower() in choice:
      found_room = room_info.adjacent[index]

  # Code that find the item you say in your input
  found_item = ""
  for index, item in enumerate(room_info.items):
    if item.lower() in choice:
      found_item = room_info.items[index]
  
  # Returns stuff ya know
  return choice, found_room, found_item


# garbage code
def look_room(room_name, current_room):
  # Get the information for the room
  found_room_info = rooms.get(found_room)
  # Check if the room is locked
  if not found_room_info.locked:
    current_room = found_room
  
  # If it is locked, print the room clue!
  else:
    print2(found_room_info.clue)
    print2("Type \"back\" to go back.")
    
    # Loop until the player answers correctly or says back to go back
    while True:
      answer = input(colour(31, "> ")).lower()

      # If the answer is "back", just break out of one loop
      if answer == "back":
        leave = False
        break
      
      elif found_room_info.answer[0] == "~":
        if found_room_info.answer[1:] in answer and found_room_info.answer[1:] in inventory:
          leave = True
          break

      else:
        if answer in found_room_info.answer:
          # This is kinda jank but I used this so I could break out of two loops easily
          leave = True
          break
      
      is_inventory(answer)

      help(answer, 31)

    # If leave is true, break out of the main loop
    if leave:
      found_room_info.locked = False
      current_room = found_room
  
  return current_room


# I hate that I have to make this a function as it is gonna be jank but whatever :(
def look_item(item_name, previous_item):
  # Gets the item information and uses a while loop to make sure the item found is in the correct room
  item_info = items.get(item_name)
  print_item_info(item_name)
  clue = False
  inside = None
  while True:
    answer = input(colour(34, "> ")).lower()

    if answer == "back":
      break
    
    # Check if the player command is one of these
    elif answer in ["look at", "open", "unlock", "inspect", "clue"]:
      # If there is no clue for the item
      if item_info.clue is None:
        # Check to see if there are items inside
        if item_info.inside is None:
          print2("You can't inspect this.")
        else:
          inside = item_info.inside
          print2("You found", colour(34, ", ".join(inside).title()))
      # If there is a clue
      else:
        clue = True
        print2(item_info.clue)

    # Check if the player command is one of these
    elif answer in ["pick up", "pickup", "take", "acquire", "yoink", "grab"]:
      # Check if the item can be picked up
      if item_info.pickup:
        inventory.append(item_name)
        print2("You picked up", colour(34, item_name.title()))
      # If the item cannot be picked up
      else:
        print2("You can't pick this up.")

    # If the player has asked for the clue, start accepting the answer
    if clue:
      # If the answer has a tilde before the word, the item needs to be in the players inventory
      if item_info.answer[0] == "~":
        # Make sure the answer matches and the item is in the players inventory
        if item_info.answer[1:] in answer and item_info.answer[1:] in inventory:
          # Set inside to what item is inside the unlocked item
          inside = item_info.inside
          print2("You found", colour(34, ", ".join(inside).title()))
      # If the item doesn't need to be in the players inventory
      else:
        if item_info.answer in answer:
          inside = item_info.inside
          print2("You found", colour(34, ", ".join(inside).title()))

    # If the player inside variable is no longer None
    if inside is not None:
      # Loops through all items inside of the unlocked item
      for index, item in enumerate(inside):
        # If the player said the name of the item, look at that item
        if item.lower() in answer:
          look_item(inside[index], item_name)

    # Check if the player is checking their inventory
    is_inventory(answer)

    # Check if the player is checking the commands
    help(answer, 34)
  
  # After the item loop is broken, print the previous item info or the room info
  if previous_item is None:
    print_room_info(current_room)
  else:
    print_item_info(previous_item)




# READING .TXT FILE!
file = open(file_name, "r")
for line in file.readlines():


  # Skips any comments in the .txt file
  if line[0] == "#":
    continue


  # Removes the \n found at the end of each line to make reading and using the text easier
  line = line.rstrip()


  # Looks for what variable or class needs to be created / changed
  if var == "":
    # "string" in line might have to be changed to line == "string"
    if line.lower() == "introduction":
      var = "introduction"
    elif line.lower() == "starting room":
      var = "starting room"
    elif line.lower() == "end room":
      var = "end room"
    elif line.lower() == "item":
      var = "item"
    elif line.lower() == "room":
      var = "room"


  # Checks to see if the current line is a newline
  elif line == "":
    if var == "item":
      # Had to do this bc I couldn't do it in one line due to needing to make sure of the len() so the program doesn't fail
      pickup = False
      if len(class_placeholder) > 2 :
        if class_placeholder[2].lower() == "true":
          pickup = True
      # Adds the item to the dictionary. Uses inline if and else for empty spots and .split() for lists
      items[class_placeholder[0].lower()] = Item( # Item name is the dictionary key
                                            class_placeholder[1], # Description
                                            pickup, # If the item can be picked up
                                            None if len(class_placeholder) < 4 else None if class_placeholder[3] == "None" else class_placeholder[3], # Clue
                                            None if len(class_placeholder) < 5 else None if class_placeholder[4] == "None" else class_placeholder[4].lower(), # Answer
                                            None if len(class_placeholder) < 6 else class_placeholder[5].lower().split(", "), # What items are inside
                                            True if len(class_placeholder) == 6 else False # If the item is locked
                                            )
    elif var == "room":
      # Does the same as above
      rooms[class_placeholder[0].lower()] = Room( # Room name is the dictionary key
                                            class_placeholder[1], # Description
                                            class_placeholder[2].lower().split(", "), # Adjacent rooms
                                            class_placeholder[3].lower().split(", "), # Items in the room
                                            None if len(class_placeholder) < 5 else class_placeholder[4], # Clue
                                            None if len(class_placeholder) < 5 else class_placeholder[5].lower(), # Answer
                                            True if len(class_placeholder) == 6 else False # Whether or not the room is locked
                                            )
    elif var == "end room":
      # Sets the end room as one of the rooms
      rooms[class_placeholder[0].lower()] = Room( # Room name is the dictionary key
                                            class_placeholder[1], # Description
                                            None, # Adjacent rooms are not needed in the exit room
                                            None, # Items are not needed in the exit room
                                            class_placeholder[2], # Clue
                                            class_placeholder[3].lower(), # Answer
                                            True # Make the room locked (for obvious reasons)
                                            )
      # Gets the end_room name for later
      end_room = class_placeholder[0].lower()
    
    var = ""
    class_placeholder.clear()
  

  # If var is not blank, create a new class variable or change a variable
  else:
    if var == "introduction":
      introduction = line
    elif var == "starting room":
      start_room = line.lower()
    elif var == "item" or var == "room" or var == "end room":
      class_placeholder.append(line)




# GAME LOOP!

# Pre-game settings and other stuff
print("Would you like to enable scrolling text?")
while True:
  # Get player input
  answer = input(colour(35, "> "))

  # If the player answers yes, enable scrolling text
  if "yes" in answer or answer == "y":
    text = "scroll"
    break
  
  # If the player answers no, don't enable scrolling text
  elif "no" in answer or answer == "n":
    break

  # If none of the above, answer isn't an option
  else:
    print("That isn't an option.")

print2("***")
commands(35)
print2("***")
print2(introduction)
print2("Press enter to continue.")
input("")

# Sets the room that the player will start in!
current_room = start_room
print_room_info(current_room)


# Actual game loop
while True:

  # Get player input
  choice, found_room, found_item = player_input(35)
  
  # If the player input includes a room name
  if found_room:

    # Check if the room is locked and do all that stuff
    next_room = look_room(found_room, current_room)

    # If the current room is not the next room? I honestly don't remember why I did this oops 0-0
    if current_room != next_room:
      
      # Check to see if the next_room is the exit
      if next_room == end_room:
        break
      
      current_room = next_room
      print_room_info(current_room)
  

  # If the player input includes a item name
  elif found_item:
    look_item(found_item, None)

# The player escaped!
print2("You successfully escaped! Congrats!")