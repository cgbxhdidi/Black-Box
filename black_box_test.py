import unittest
import black_box as bb

class TestBlackBox(unittest.TestCase):

    def setUp(self):
        global Locations, l_mark, t_mark, r_mark, b_mark, Loc_Marks, N
        bb.Locations = [(1, 1), (3, 7), (5, 0), (6, 3)]
        E = ' '
        bb.l_mark = [E, E, E, E, E, E, E, E]
        bb.r_mark = [E, E, E, E, E, E, E, E]
        bb.t_mark = [E, E, E, E, E, E, E, E]
        bb.b_mark = [E, E, E, E, E, E, E, E]
        bb.Loc_Marks = []
        bb.N = 0

    def test_new_game(self):
        self.assertEqual(bb.Locations, [(1, 1), (3, 7), (5, 0), (6, 3)])
        bb.new_game((1, 5), (2, 7), (6, 0), (4, 3))
        self.assertEqual(bb.Locations, [(1, 5), (2, 7), (6, 0), (4, 3)])

    def test_one_step(self):
        self.assertEqual(bb.one_step(((2, 1), 'b')), None)
        self.assertEqual(bb.one_step(((2, 6), 'l')), ((2, 6), 'b'))

    def test_shoot(self):
        self.assertEqual(bb.shoot('2l'), None)
        self.assertEqual(bb.shoot('3l'), None)
        self.assertEqual(bb.shoot('5b'), '8r')
        self.assertEqual(bb.shoot('3b'), '8l')

    def test_mark(self):
        E = ' '
        bb.mark('3l')
        self.assertEqual(bb.l_mark, [E, E, 'H', E, E, E, E, E])
        bb.mark('5b')
        self.assertEqual(bb.b_mark, [E, E, E, E, 'a', E, E, E])
        self.assertEqual(bb.r_mark, [E, E, E, E, E, E, E, 'a'])

    def test_toggle(self):
        bb.toggle(3, 4)
        self.assertEqual(bb.Loc_Marks, [(2, 3)])
        bb.toggle(5, 6)
        self.assertEqual(bb.Loc_Marks, [(2, 3), (4, 5)])
        bb.toggle(1, 7)
        self.assertEqual(bb.Loc_Marks, [(2, 3), (4, 5), (0, 6)])

    def test_score(self):
        self.assertEqual(bb.score(), 60)
        bb.toggle(3, 4)
        bb.mark('3l')
        self.assertEqual(bb.score(), 49)
        
unittest.main()
