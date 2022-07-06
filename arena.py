import operator

from constants import DROWNED, KILLED, ALIVE
from fight import Fight
from position import Position


# This class is the 8x8 board on which the game is played
class Arena:
    Board = list()

    # creating a 8x8 board when the game is started so that we get initial positions for all the items and knights
    def __init__(self):
        for row in range(8):
            row = [Position(row, col) for col in range(8)]
            self.Board.append(row)

    # below-mentioned method provides information about the next move the knight is going to make on the board
    def movements(self, direction, position):
        row = position.row
        col = position.col
        if direction == 'S':
            row += 1
        elif direction == 'N':
            row -= 1
        elif direction == 'W':
            col -= 1
        elif direction == 'E':
            col += 1
        if row > 7 or col > 7 or row < 0 or col < 0:
            return None
        return self.Board[row][col]

    # created below is a method where a knight is sent to do important changes in states of objects on board after
    # drowning
    @staticmethod
    def drown_knight(knight):
        item = knight.item
        position = knight.position
        if item:
            item.is_equipped = False
            knight.item = None
            position.items.append(item)
            item.position = position
        knight.attack = knight.defence = 0
        knight.status = DROWNED

    # created below is a method where a knight is sent to do important changes in states of objects on board after
    # being killed by some other knight
    @staticmethod
    def kill_knight(knight):
        item = knight.item
        position = knight.position
        if item:
            item.is_equipped = False
            knight.item = None
            position.items.append(item)
        knight.status = KILLED
        knight.attack = knight.defence = 0

    # below method moves the knights on the board doing necessary changes in states
    def move_knight(self, knight, direction):
        if not knight.status == DROWNED and not knight.status == KILLED:
            current_position = self.movements(direction, knight.position)
            if not current_position:
                self.drown_knight(knight)
                knight.position = current_position
            else:
                if current_position.items and not knight.item:
                    item = sorted(current_position.items, key=operator.attrgetter('priority'))[0]
                    knight.item = item
                    item.is_equipped = True
                    item.position = None
                    current_position.items.remove(item)
                if current_position.knight and current_position.knight.status == ALIVE:
                    winner, loser = Fight.fight(knight, current_position.knight)
                    self.kill_knight(loser)
                    loser.position = current_position
                    knight = winner
                knight.position.knight = None
                knight.position = current_position
                current_position.knight = knight
                if knight.item:
                    knight.item.position = knight.position
