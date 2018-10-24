### Game File

# Imports here
import cmd
import textwrap
import sys
import os
import time
import random
import world_map
# End Imports

# Global Variables
screen_width = 100

# Player Setup
class player:
    def __init__(self):
        self.name = ''
        self.hp = None
        self.mp = 0
        self.status = []
        self.location = 'start'

myPlayer = player()

# Title Screen Settings
def title_screen_selections():
    option = input('> ')
    print('Please enter a command')
    if option.lower() == ('play'):
        start_game() ### start_game is a placeholder that doesn't exist yet
    elif option.lower() == ('help'):
        help_menu() ### PLACEHOLDER
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command')
        if option.lower() == ('play'):
            start_game() ### start_game is a placeholder that doesn't exist yet
        elif option.lower() == ('help'):
            help_menu() ### PLACEHOLDER
        elif option.lower() == ('quit'):
            sys.exit()
            
def title_screen():
    os.system('clear')
    print('#######################')
    print('# Welcome to the RPG! #')
    print('#######################')
    print('#      - Play -       #')
    print('#      - Help -       #')
    print('#      - Quit -       #')
    print('#######################')
    title_screen_selections()
    
def help_menu():
    print('#######################')
    print('#      - HELP -       #')
    print('#######################')
    print('# Use arrows to move  #')
    print('#                     #')
    print('#   Type a command    #')
    print('#  to do that action  #')
    print('#######################')
    title_screen_selections()
    
    
# Game Functionality
def start_game():
    pass


# Mapping
ZONENAME = ''
DESCRIPTION = 'description'
EXPLANATION = 'explanation'
CLEARED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

