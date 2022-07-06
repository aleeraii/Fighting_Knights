# Below-mentioned class represents the positions of the items and knights on the board
class Position:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.knight = None
        self.items = list()

    def get_pos(self):
        return [self.row, self.col]
