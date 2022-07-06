# Below class Item represents contains the information related to items present on the board
class Item:

    def __init__(self, item_id, name, priority, position=None, attack=0, defence=0):
        self.id = item_id
        self.name = name
        self.attack = attack
        self.defence = defence
        self.position = position
        self.priority = priority
        self.is_equipped = False

        position.items.append(self)

