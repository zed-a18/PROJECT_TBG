from room import Room
from character import Character, Enemy, Friend
from item import Item

kitchen = Room()
kitchen.set_name("Kitchen")
dining_hall = Room()
dining_hall.set_name("Dining Hall")
ballroom = Room()
ballroom.set_name("Ballroom")

kitchen.set_description(
    "A dank and dirty room buzzing with flies - a single lamp lighting the room. You see a mysterious glowing cheese in the cabinet and brains on the table..."
)
dining_hall.set_description(
    "A large room with dusty ornate golden furniture. Candlelight spread around the room to keep it lit. There is a key on the floor labelled Storage Key."
)
ballroom.set_description(
    "A vast room with a shiny wooden floor. The moonlight coming through the large windows lighting up the room. There is a storage door that can be opened with a key."
)


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "Dave is a smelly zombie")
dave.set_conversation("Braaaaiiiinns...")
dave.set_weakness("cheese")
dave.set_favourite("brains")

dining_hall.set_character(dave)

yuna = Friend("Yuna", "Yuna a young women with long black hair wearing a white dress")
yuna.set_conversation(
    "Hello, my name is Yuna. please help me find my left slipper so that I can leave. I lost it in the Ballroom"
)
yuna.set_gift_item("Slipper")
kitchen.set_character(yuna)

key = Item()
key.set_name("Ballroom Key")
key.set_description("An old key with a tag: Storage Key")
yuna.add_item(key)

cheese = Item()
cheese.set_name("Cheese")
cheese.set_description(
    "Stinky cheese with a weird glow...Could this be used for something?"
)

slipper = Item()
slipper.set_name("Slipper")
slipper.set_description("Left splipper belonging to a women")

brains = Item()
brains.set_name("Brains")
brains.set_description("Fresh brains...Could this belong to a human?")

player = Character("Adventurer", "...")

current_room = kitchen

playerinput = input

playerinput = True
while playerinput:
    start = Room()
    start.start()
    begin = input("> ").lower()
    if begin == "yes":
        playerinput = False
        break
    elif begin == "no":
        print("You decide to leave...")
        print("[Game Over!]")
        exit()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

while True:
    print(
        f"\n[MOVE to a different room using: 'north', 'east', 'south' or 'west'] [INTERACT with 'talk', 'bribe', 'gift', 'fight', 'look' or 'inventory']\n"
    )
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
        else:
            print("You are in the room alone.")

    elif command == "gift":
        if isinstance(inhabitant, Friend):
            print(f"Type the item name {player.inventory} you want to Gift with:")
            give_item = input("> ").lower()
            if give_item in player.inventory:
                give_result = inhabitant.gift(give_item)
                if give_result:
                    player.inventory.remove(give_item)
                    print(f"You gifted {give_item} to {inhabitant.get_name()}")
                else:
                    print(f"{inhabitant.get_name()} declined your gift")
            else:
                print(f"You don't have {give_item} in your inventory")
        else:
            print("There is no one to gift in the room")

    elif command == "fight":
        if inhabitant:
            print(f"Type the item name {player.inventory} you want to Fight with:")
            fight_with = input("> ").lower()
            if fight_with in player.inventory:
                fight_result = inhabitant.fight(fight_with)
                if fight_result:
                    player.inventory.remove(fight_with)
                    current_room.remove_character()
                    print("Dave has been defeated. You can now move to the Ballroom")
                else:
                    print("Game Over")
                    break
            else:
                print(f"You don't have {fight_with} in your inventory")
        else:
            print("There is no one to fight here")

    elif command == "bribe":
        if inhabitant:
            print(f"Type the item name {player.inventory} you want to Bribe with:")
            bribe_with = input("> ").lower()
            if bribe_with in player.inventory:
                bribe_result = inhabitant.bribe(bribe_with)
                if bribe_result:
                    player.inventory.remove(bribe_with)
                    current_room.remove_character()
                    print("Dave has been removed. You can now move west!")
                else:
                    print("Game Over")
                    break
            else:
                print(f"You don't have {bribe_with} in your inventory")
        else:
            print("There is no one to bribe here")

    elif command == "inventory":
        if player.inventory:
            print(", ".join(player.inventory))
        else:
            print("You have no items in your inventory.")

    elif command == "look":
        if current_room.get_name() == "Kitchen":
            print(
                "There is a glowing piece of cheese in the cabinet and brains on the table."
            )
            if "Cheese" not in player.inventory:
                player.add_item("Cheese")
                print("You put Cheese in your inventory.")
            if "Brains" not in player.inventory:
                player.add_item("Brains")
                print("You put Brains in your inventory.")
            print("---------------------------")
        elif current_room.get_name() == "Dining Hall":
            print("There is a key on the floor labelled Storage Key.")
            if "Ballroom Key" not in player.inventory:
                player.add_item("Ballroom Key")
                print("You put Ballroom Key in your inventory.")
                print("---------------------------")
        elif current_room.get_name() == "Ballroom":
            print("There is a storage door.")
            if "Ballroom Key" in player.inventory:
                print("Would you like to use the key? [yes / no]")
                use_key = input("> ").lower()
                if use_key == "yes":
                    print(
                        "You open the storage door with the key. You find a slipper held by a dead man missing his brains. You yank the slipper out of his hand and put it in your inventory."
                    )
                    player.add_item("Slipper")
                    print(
                        "You return the slipper to Yuna and decide to leave with her..."
                    )
                    print("Game Complete!")
                    break
                elif use_key == "no":
                    print("You leave the storage door alone.")
            else:
                print("Storage door is locked. You need a key to open it.")
        else:
            print("You look around, but there's nothing of interest here.")
