from room import Room
from player import Player
from item import Item

# Declare items

dusty_pickaxe = Item('dusty pickaxe', 'Someone must have left this here')
torch = Item('musty torch', 'Anyone have a match?')
rope = Item('worn rope', 'Something chewed on the end of this...')
shiny_rocks = Item('shiny rocks', 'These are kind of pretty')
broken_chest = Item('broken chest', 'This used to be useful I guess')

# Declare all the rooms
outside = Room("Outside Cave Entrance",
                "North of you, the cave mount beckons", [dusty_pickaxe])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [torch])

overlook =  Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [rope])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [shiny_rocks])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [broken_chest])

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player('Rose', outside)

# Write a loop that:
while True:
    # * Prints the current room name
    print(player_one.current_room.name)
    
    # * Prints the current description (the textwrap module might be useful here).
    print(player_one.current_room.description)

    # Print current inventory
    for i in range(len(player_one.inventory)):
        print(f'{player_one.name} has {i+1}: {player_one.inventory[i].name} in inventory')

    # Print items in current room
    print('Looking around you see...')
    for i in range(len(player_one.current_room.items)):
        print(f'{i+1}: {player_one.current_room.items[i].name}')

    base_choice = input('What do you want to do? (get, drop, travel): ')

    if base_choice == 'get':
        if len(player_one.current_room.items) >= 1:
            which_item = input("Which item do you want? (#): ")
            player_one.get_item(player_one.current_room.items[int(which_item)-1])
            player_one.current_room.items[int(which_item)-1].on_take()
            player_one.current_room.remove(player_one.current_room.items[int(which_item)-1])
    
    elif base_choice == 'drop':
        if len(player_one.inventory) >= 1:
            to_drop = input("What item do you want to drop? (#): ")
            player_one.drop_item(player_one.inventory[int(to_drop)-1])
            print(f'Dropped an item!')

    # * Waits for user input and decides what to do.
    choice = input("Type q to quit or\nWhere do you want to go? (n, e, s, w) : ")

    # If the user enters "q", quit the game.
    if choice == 'q':
        break
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif choice == 'n' and player_one.current_room.n_to:
        player_one.current_room = player_one.current_room.n_to

    elif choice == 'e' and player_one.current_room.e_to:
        player_one.current_room = player_one.current_room.e_to

    elif choice == 's' and player_one.current_room.s_to:
        player_one.current_room = player_one.current_room.s_to

    elif choice == 'w' and player_one.current_room.w_to:
        player_one.current_room = player_one.current_room.w_to
        
# Print an error message if the movement isn't allowed.
    else:
        print("Whoops! You can't go that way. Try another direction")
