### Title Screen Settings

def title_screen_selections():
    option = input('> ')
    print('Select a command')
    if option.lower == 'help':
        help_menu()
    elif option.lower == 'settings':
        settings_menu()
    elif option.lower == 'quit':
        quit_menu()
    else:
        print('Please select a valid option')

def title_screen():
    os.system('clear')
    print('#######################')
    print('#  Kingdom Reclaimer  #')
    print('#######################')
    print('#      - Play -       #')
    print('#      - Help -       #')
    print('#    - Settings -     #')
    print('#      - Quit -       #')
    print('#######################')
    title_screen_selections()
    
def help_menu():
    os.system('clear')
    print('#######################')
    print('#      - HELP -       #')
    print('#######################')
    print('# Use arrows to move  #')
    print('#                     #')
    print('#   Type a command    #')
    print('#  to do that action  #')
    print('#######################')
    title_screen_selections()
    
def settings_menu():
    pass

def quit_menu():
    pass
            
