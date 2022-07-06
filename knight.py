from constants import ALIVE


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
