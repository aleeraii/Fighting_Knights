import unittest
from item import Item
from arena import Arena
from knight import Knight
from constants import ALIVE, KILLED, KNIGHTS_MAPPING, DROWNED


class TestCase(unittest.TestCase):
    def setUp(self):
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

    def test_move_knight(self):
        self.arena.move_knight(self.knight_r, 'S')
        self.arena.move_knight(self.knight_r, 'E')
        self.arena.move_knight(self.knight_r, 'E')

        self.arena.move_knight(self.knight_g, 'N')
        self.arena.move_knight(self.knight_g, 'N')

        self.assertEqual(self.knight_r.position.row, 1)
        self.assertEqual(self.knight_r.position.col, 2)

        self.assertEqual(self.knight_g.position.row, 5)
        self.assertEqual(self.knight_g.position.col, 7)

    def test_equip_knight(self):
        self.arena.move_knight(self.knight_r, 'S')
        self.arena.move_knight(self.knight_r, 'E')
        self.arena.move_knight(self.knight_r, 'E')
        self.arena.move_knight(self.knight_r, 'S')

        self.arena.move_knight(self.knight_g, 'N')
        self.arena.move_knight(self.knight_g, 'N')
        self.arena.move_knight(self.knight_g, 'W')
        self.arena.move_knight(self.knight_g, 'W')

        self.assertEqual(self.knight_r.item, self.axe)

        self.assertEqual(self.knight_g.item, self.helmet)

    def test_status_knight(self):
        self.arena.move_knight(self.knight_y, 'E')

        self.arena.move_knight(self.knight_b, 'N')
        self.arena.move_knight(self.knight_b, 'N')
        self.arena.move_knight(self.knight_b, 'N')
        self.arena.move_knight(self.knight_b, 'N')
        self.arena.move_knight(self.knight_r, 'S')
        self.arena.move_knight(self.knight_r, 'S')
        self.arena.move_knight(self.knight_r, 'S')
        self.arena.move_knight(self.knight_r, 'S')

        self.assertEqual(self.knight_y.status, DROWNED)
        self.assertEqual(self.knight_b.status, KILLED)
        self.assertEqual(self.knight_r.status, ALIVE)

    def test_fight(self):
        moves = [
            ['R', 'S'], ['R', 'S'], ['R', 'E'], ['R', 'E'], ['G', 'N'], ['G', 'N'], ['G', 'W'], ['G', 'W'], ['G', 'N'],
            ['G', 'N'], ['G', 'W'], ['G', 'W'], ['R', 'S'], ['R', 'E']
        ]
        for knight, move in moves:
            self.arena.move_knight(getattr(self, KNIGHTS_MAPPING[knight]), move)

        self.assertEqual(self.knight_r.position.row, 3)
        self.assertEqual(self.knight_r.position.col, 3)
        self.assertEqual(self.knight_r.item, self.axe)
        self.assertEqual(self.knight_r.status, ALIVE)

        self.assertEqual(self.knight_g.position.row, 3)
        self.assertEqual(self.knight_g.position.col, 3)
        self.assertEqual(self.knight_g.item, None)
        self.assertEqual(self.knight_g.status, KILLED)


if __name__ == '__main__':
    unittest.main(verbosity=2)
