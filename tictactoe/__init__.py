"""Tic Tac Toe package.

Makes `tictactoe` importable so tests can do `from tictactoe.game import TicTacToe`
and `from tictactoe.ai import best_move`.

Modules:


- game: Core game logic (TicTacToe class)
- ai: AI strategies (minimax, random)
- cli: Command-line interface to play
"""
from .game import TicTacToe
from .ai import best_move

__all__ = ["TicTacToe", "best_move"]

#__all__ = ["game", "ai"]