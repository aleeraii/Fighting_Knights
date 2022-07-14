from constants import ALIVE
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
    def get_next_valid_position(self, direction, position):
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
        next_valid_position = self.get_next_valid_position(direction, knight.position)
        if not next_valid_position:
            knight.drown()
            return None

        if next_valid_position.items and not knight.item:
            knight.equip(next_valid_position)

        if next_valid_position.knight and next_valid_position.knight.status == ALIVE:
            winner, loser = Fight.fight(knight, next_valid_position.knight)
            loser.kill(next_valid_position)
            knight = winner

        knight.move(next_valid_position)
