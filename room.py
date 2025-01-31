from character import Character, Enemy, Friend
from item import Item


class Room:
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_rooms = {}
        self.next_room = None
        self.character = None
        self.item = None

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description
        return self.description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name
        return self.name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def remove_character(self):
        self.character = None

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def set_objective(self, objective):
        self.objective = objective

    def get_objective(self):
        return self.objective

    def get_details(self):
        print(f"Room: {self.name}")
        print("---------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    def start(self):
        print(
            "You find yourself in the backyard of a building and see a door leading to a kitchen...Enter? [yes / no]"
        )

    def move(self, direction):
        if direction in self.linked_rooms:
            next_room = self.linked_rooms[direction]
            if (
                next_room
                and next_room.name == "Ballroom"
                and self.name == "Dining Hall"
            ):
                if self.character and isinstance(self.character, Enemy):
                    print(
                        "Dave blocks your path. You must deal with him first by Fight or Bribe"
                    )
                    return self  # Return the current room if Dave is still present
            return next_room if next_room else self
        else:
            print("You can't go that way")
            return self

    def check_and_remove_enemy(self, combat_item, favourite_item):
        if self.character and isinstance(self.character, Enemy):
            if (
                combat_item == self.character.weakness
                or favourite_item == self.character.favourite
            ):
                print(
                    f"{self.character.name} has been dealt with and is no longer blocking your path"
                )
                self.remove_character()
                return True
            else:
                print(
                    f"{self.character.name} is still blocking your path - you must Fight or Bribe"
                )
                return False

    def fight(self, item_used):
        if self.character and isinstance(self.character, Enemy):
            if self.check_and_remove_enemy(item_used):
                print(f"You have defeated {self.character.name}!")
            else:
                print(f"{self.character.name} overpowers you. Game Over!")
                exit()
        else:
            print("There is no one to fight here.")

    def bribe(self, item_used):
        if self.character and isinstance(self.character, Enemy):
            if self.check_and_remove_enemy(item_used):
                print(
                    f"You have successfully bribed {self.character.name} and he leaves."
                )
            else:
                print(
                    f"{self.character.name} refuses your offer and attacks! Game Over!"
                )
                exit()
        else:
            print("There is no one to bribe here.")
