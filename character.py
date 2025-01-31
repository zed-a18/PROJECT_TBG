class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = []

    def describe(self):
        print(f"{self.name} is in this room...")
        print(self.description)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.pop(item)

    def get_inventory(self):
        return self.inventory

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"[{self.name} doesn't want to talk to you]")

    def fight(self, combat_item):
        print(f"[{self.name} doesn't want to fight you]")
        return True

    def bribe(self, bribe_item):
        print(f"[{self.name} can't be bribed.]")
        return True

    def get_name(self):
        return self.name


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def set_favourite(self, favourite_item):
        self.favourite = favourite_item

    def get_favourite(self):
        return self.favourite

    def gift(self, gift_item):
        self.gift_item = gift_item
        print(f"[{self.name} doesn't want any gifts.]")

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You have defeated {self.name} with the {combat_item}")
            print("---------------------------")
            return True  # Return True if the fight is successful
        else:
            print(f"{self.name} has defeated you")
            print("---------------------------")
            return False  # Return False if the fight is unsuccessful

    def bribe(self, bribe_item):
        if bribe_item == self.favourite:
            print(
                f"[{self.name} takes the item: {bribe_item} - They have accepted your bribe.]"
            )
            print("---------------------------")
            return True  # Return True if the bribe is successful
        else:
            print(f"[{self.name} has no interest in the item: {bribe_item}.]")
            print("---------------------------")
            return False  # Return False if the bribe is unsuccessful


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def set_gift_item(self, gift_item):
        self.gift_item = gift_item

    def get_gift_item(self):
        return self.gift_item

    def gift(self, give_gift):
        if give_gift == self.gift_item:
            print(f"[{self.name} accepts your gift: {give_gift} and thanks you.]")
            print("---------------------------")
        else:
            print(f"[{self.name} decliens your gift: {give_gift}.]")
            print("---------------------------")
