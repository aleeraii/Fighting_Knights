import json
import os


class InputOutputData:

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
