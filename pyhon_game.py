import sys

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connected_rooms = {}

    def connect_room(self, room, direction):
        self.connected_rooms[direction] = room

    def get_room_in_direction(self, direction):
        return self.connected_rooms.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Game:
    def __init__(self):
        self.create_world()
        self.current_room = self.rooms['Hall']
        self.inventory = []

    def create_world(self):
        hall = Room("Hall", "A spacious hall with a grand staircase.")
        kitchen = Room("Kitchen", "A clean kitchen with shiny utensils.")
        library = Room("Library", "A quiet library filled with books.")

        hall.connect_room(kitchen, "east")
        hall.connect_room(library, "west")
        kitchen.connect_room(hall, "west")
        library.connect_room(hall, "east")

        key = Item("Key", "A small rusty key.")
        book = Item("Book", "An old dusty book.")

        hall.add_item(key)
        library.add_item(book)

        self.rooms = {
            "Hall": hall,
            "Kitchen": kitchen,
            "Library": library
        }

    def start(self):
        print("Welcome to the Adventure Game!")
        self.show_current_room()

    def show_current_room(self):
        print(f"\nYou are in the {self.current_room.name}.")
        print(self.current_room.description)
        if self.current_room.items:
            print("You see the following items:")
            for item in self.current_room.items:
                print(f"- {item.name}: {item.description}")
        print("\nAvailable directions:")
        for direction in self.current_room.connected_rooms:
            print(f"- {direction}")

    def move(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room:
            self.current_room = next_room
            self.show_current_room()
        else:
            print("You can't go that way!")

    def pick_up(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.current_room.remove_item(item)
                self.inventory.append(item)
                print(f"You picked up the {item.name}.")
                return
        print("There is no such item here.")

    def show_inventory(self):
        print("\nYour inventory:")
        for item in self.inventory:
            print(f"- {item.name}: {item.description}")
        if not self.inventory:
            print("You are not carrying any items.")

    def handle_command(self, command):
        if command in ["north", "south", "east", "west"]:
            self.move(command)
        elif command.startswith("pick up "):
            item_name = command[8:]
            self.pick_up(item_name)
        elif command == "inventory":
            self.show_inventory()
        elif command == "quit":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("I don't understand that command.")

    def play(self):
        self.start()
        while True:
            command = input("\nWhat do you want to do? ")
            self.handle_command(command)

if __name__ == "__main__":
    game = Game()
    game.play()
