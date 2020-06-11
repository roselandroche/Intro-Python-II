# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room

        self.inventory = []

    def get_item(self, item):
        self.inventory.append(item)
        print(f'{self.name} picked up {item}!')