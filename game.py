from item import Item
from arena import Arena
from knight import Knight
from constants import KNIGHTS_MAPPING, ALIVE
from input_output_data import InputOutputData


# this class represents the initial setup of the game board including the positions for items and knights
class Game:

    def __init__(self):
        self.arena = Arena()
        position = self.arena.Board
        self.axe = Item('A', 'axe', 4, position[2][2], attack=2)
        self.dagger = Item('D', 'dagger', 2, position[2][5], attack=1)
        self.helmet = Item('H', 'helmet', 1, position[5][5], defence=1)
        self.magic_staff = Item('M', 'magic_staff', 3, position[5][2], attack=1, defence=1)

        self.knight_r = Knight('R', 'red', position[0][0])
        self.knight_g = Knight('G', 'green', position[7][7])
        self.knight_b = Knight('B', 'blue', position[7][0])
        self.knight_y = Knight('Y', 'yellow', position[0][7])

    # consider this as the root method which controls the program from reading input file to writing output file
    def run(self, input_moves_file, output_file):
        iodata = InputOutputData()
        moves = iodata.read_moves(input_moves_file)
        for knight, move in moves:
            knight = getattr(self, KNIGHTS_MAPPING[knight])
            if knight.status == ALIVE:
                self.arena.move_knight(knight, move)

        iodata.write_output(output_file,
                            (self.knight_r, self.knight_b, self.knight_g, self.knight_y),
                            (self.magic_staff, self.helmet, self.dagger, self.axe))


if __name__ == '__main__':
    game = Game()
    game.run('moves.txt', 'final_state.json')   # please provide the input moves file and output json file names here
