import json
import os.path
import operator

from constants import ALIVE, DROWNED, KILLED, KNIGHTS_MAPPING


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


# Below-mentioned class represents the positions of the items and knights on the board
class Position:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.knight = None
        self.items = list()

    def get_pos(self):
        return [self.row, self.col]


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


class Fight:

    # this method takes in two knights as attacker and defender and returns the same two knights as winner and loser
    # after fight between them
    @staticmethod
    def fight(attacker, defender):
        attacker.attack += 0.5
        attacker_score = attacker.attack
        defender_score = defender.defence
        if attacker.item:
            attacker_score += attacker.item.attack
        if defender.item:
            defender_score += defender.item.defence
        return (attacker, defender) if attacker_score > defender_score else (defender, attacker)


class DataFlow:

    # this method reads the input moves file in a standard manner
    @staticmethod
    def read_moves(file_path):
        if not os.path.exists(file_path):
            raise Exception('Invalid Moves File Path')
        moves_file = open(file_path, 'r').read().strip().splitlines()
        moves_file.pop(0)
        moves_file.pop(-1)
        return [move.strip().split(':') for move in moves_file if move]

    # this method returns the outputs in the form of a json file
    @staticmethod
    def write_output(output_file, knights, items):
        output_moves = dict()
        for knight in knights:
            output_moves[knight.name] = [knight.position.get_pos() if knight.position else None, knight.status,
                                         knight.item.name if knight.item else None,
                                         knight.attack + knight.item.attack if knight.item else knight.attack,
                                         knight.defence + knight.item.defence if knight.item else knight.defence]
        for item in items:
            output_moves[item.name] = [item.position.get_pos(), item.is_equipped]
        with open(output_file, 'w') as file:
            file.write(json.dumps(output_moves))


# this class represents the initial setup of the game board including the positions for items and knights
class Game:

    def __init__(self):
        self.arena = Arena()
        position = self.arena.Board
        self.axe = Item('A', 'axe', 4, position[2][2], attack=2)
        self.dagger = Item('D', 'dagger', 3, position[2][5], attack=1)
        self.helmet = Item('H', 'helmet', 1, position[5][5], defence=1)
        self.magic_staff = Item('M', 'magic_staff', 3, position[5][2], attack=1, defence=1)

        self.knight_r = Knight('R', 'red', position[0][0])
        self.knight_g = Knight('G', 'green', position[7][7])
        self.knight_b = Knight('B', 'blue', position[7][0])
        self.knight_y = Knight('Y', 'yellow', position[0][7])

    # consider this as the root method which controls the program from reading input file to writing output file
    def run(self, input_moves_file, output_file):
        iodata = DataFlow()
        moves = iodata.read_moves(input_moves_file)
        for knight, move in moves:
            self.arena.move_knight(getattr(self, KNIGHTS_MAPPING[knight]), move)

        iodata.write_output(output_file, (self.knight_r, self.knight_b, self.knight_g, self.knight_y),
                            (self.magic_staff, self.helmet, self.dagger, self.axe))
