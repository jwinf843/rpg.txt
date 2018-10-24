from pprint import pprint

def create_world(x, y):
    map_width = x
    map_height = y
    world_map = {}

    for row in range(map_height):
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for column in range(map_width):
            our_string = ''
            our_string += alphabets[row] + str(column + 1)
            world_map.setdefault(our_string, [])
    for place in world_map:
        world_map[place].append(False)
        
    return world_map

"""
----------------
|A1|A2|A3|A4|A5|
----------------
|B1|B2|B3|B4|B5|
----------------
|C1|C2|C3|C4|C5|
----------------
|D1|D2|D3|D4|D5|
----------------
"""    

# world_map = create_world(5, 5)
# pprint(world_map)