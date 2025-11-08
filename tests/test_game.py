import unittest
from tictactoe.game import TicTacToe
from tictactoe.ai import best_move

class TestTicTacToe(unittest.TestCase):
    def test_initial_state(self):
        g = TicTacToe()
        self.assertEqual(len(g.available_moves()), 9)
        self.assertIsNone(g.winner)
        self.assertFalse(g.is_draw())

    def test_make_move_and_switch(self):
        g = TicTacToe()
        self.assertTrue(g.make_move(0))  # X
        self.assertEqual(g.current_player, 'O')
        self.assertFalse(g.make_move(0))  # occupied
        self.assertTrue(g.make_move(4))  # O
        self.assertEqual(g.current_player, 'X')

    def test_winner_row(self):
        g = TicTacToe()
        g.make_move(0)  # X
        g.make_move(3)  # O
        g.make_move(1)  # X
        g.make_move(4)  # O
        g.make_move(2)  # X wins
        self.assertEqual(g.winner, 'X')
        self.assertTrue(g.game_over())

    def test_winner_diag(self):
        g = TicTacToe()
        g.make_move(0)  # X
        g.make_move(1)  # O
        g.make_move(4)  # X
        g.make_move(2)  # O
        g.make_move(8)  # X wins
        self.assertEqual(g.winner, 'X')

    def test_draw(self):
        g = TicTacToe()
        # X O X
        # X X O
        # O X O
        moves = [0,1,2,5,3,4,8,6,7]
        for m in moves:
            self.assertTrue(g.make_move(m))
        self.assertIsNone(g.winner)
        self.assertTrue(g.is_draw())
        self.assertTrue(g.game_over())

    def test_ai_blocks_or_wins(self):
        # Case 1: AI can win immediately
        g = TicTacToe()
        g.board = ['O', 'O', None,
                   'X', 'X', None,
                   None, None, None]
        g.current_player = 'O'
        move = best_move(g, 'O')
        self.assertEqual(move, 2)
        
        # Case 2: AI blocks opponent's winning move
        g = TicTacToe()
        g.board = ['X', 'X', None,
                   None, 'O', None,
                   None, None, None]
        g.current_player = 'O'
        move = best_move(g, 'O')
        self.assertEqual(move, 2)

if __name__ == '__main__':
    unittest.main()
