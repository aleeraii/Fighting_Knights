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
    def get_next_position(self, direction, position):
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

    # below method moves the knights on the board doing necessary changes in states
    def move_knight(self, knight, direction):
        current_position = self.get_next_position(direction, knight.position)
        if not current_position:
            knight.drown()
        else:
            if current_position.items and not knight.item:
                knight.equip(current_position)
            if current_position.knight and current_position.knight.status == ALIVE:
                winner, loser = Fight.fight(knight, current_position.knight)
                loser.kill(current_position)
                knight = winner
            knight.move(current_position)
