### Title Screen Settings

# def title_screen_selections():
#     option = input('> ')
#     print('Please enter a command')
#     if option.lower() == ('play'):
#         start_game() 
#     elif option.lower() == ('help'):
#         help_menu() 
#     elif option.lower() == ('quit'):
#         sys.exit()
#     while option.lower() not in ['play', 'help', 'quit']:
#         print('Please enter a valid command')
#         if option.lower() == ('play'):
#             start_game() 
#         elif option.lower() == ('help'):
#             help_menu() 
#         elif option.lower() == ('quit'):
#             sys.exit()
            
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