# Implement a class to hold item information. This should have name and
# description attributes. This is a base class.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        pass

    def on_drop(self):
        pass