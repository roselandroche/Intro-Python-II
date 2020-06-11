from room import Room
from player import Player

# Declare all the rooms
outside = Room("Outside Cave Entrance",
                "North of you, the cave mount beckons", ['dirt', 'rocks'])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torches'])

overlook =  Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['binoculars'])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['pickaxes'])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['forgotten coins'])

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

    # Print items in current room
    if len(player_one.current_room.items) >= 1:
        for i in player_one.current_room.items:
            print(f'Looking around, you see {i}')

    # * Waits for user input and decides what to do.
    choice = input("Where do you want to go? (n, e, s, w) : ")

    # If the user enters "q", quit the game.
    if choice == 'q':
        break
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif choice == 'n' and player_one.current_room.n_to:
        player_one.current_room = player_one.current_room.n_to
        # if items exist in room, print to console

    elif choice == 'e' and player_one.current_room.e_to:
        player_one.current_room = player_one.current_room.e_to
        # if items exist in room, print to console

    elif choice == 's' and player_one.current_room.s_to:
        player_one.current_room = player_one.current_room.s_to
        # if items exist in room, print to console

    elif choice == 'w' and player_one.current_room.w_to:
        player_one.current_room = player_one.current_room.w_to
        # if items exist in room, print to console
        
# Print an error message if the movement isn't allowed.
    else:
        print("Whoops! You can't go that way. Try another direction")