import operator

from constants import ALIVE, DROWNED, KILLED


# Below-mentioned class is an information container for knights on the gaming board
class Knight:

    def __init__(self, knight_id, name, position, status=ALIVE, item=None):
        self.id = knight_id
        self.name = name
        self.status = status
        self.position = position
        self.item = item
        self.defence = 1
        self.attack = 1

        position.knight = self

    def die(self):
        item = self.item
        position = self.position
        if item:
            self.item = None
            position.items.append(item)
            item.un_equip(position)
        position.knight = None
        self.attack = self.defence = 0

    def drown(self):
        self.die()
        self.position = None
        self.status = DROWNED

    def kill(self, pos):
        self.die()
        self.position = pos
        self.status = KILLED

    def equip(self, pos):
        item = sorted(pos.items, key=operator.attrgetter('priority'))[-1]
        self.item = item
        item.equip()
        pos.items.remove(item)

    def move(self, pos):
        self.position.knight = None
        self.position = pos
        pos.knight = self
        if self.item:
            self.item.position = self.position
