from __future__ import annotations
from typing import List, Optional

class TicTacToe:
    """Core Tic Tac Toe game state and mechanics.

    Board representation: list of length 9 with values 'X', 'O', or None.
    Index mapping:
      0 | 1 | 2
      3 | 4 | 5
      6 | 7 | 8
    """

    WIN_PATTERNS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]

    def __init__(self, starting_player: str = "X"):
        if starting_player not in ("X", "O"):
            raise ValueError("starting_player must be 'X' or 'O'")
        self.board: List[Optional[str]] = [None] * 9
        self.current_player: str = starting_player
        self.winner: Optional[str] = None

    def available_moves(self) -> List[int]:
        return [i for i, v in enumerate(self.board) if v is None]

    def make_move(self, position: int) -> bool:
        """Attempt to place the current player's mark at position.

        Returns True if move succeeds; False if invalid.
        """
        if self.winner is not None:
            return False
        if position < 0 or position >= 9 or self.board[position] is not None:
            return False
        self.board[position] = self.current_player
        self._update_winner()
        if self.winner is None and not self.is_draw():
            self._switch_player()
        return True

    def _switch_player(self) -> None:
        self.current_player = "O" if self.current_player == "X" else "X"

    def _update_winner(self) -> None:
        for a, b, c in self.WIN_PATTERNS:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                return

    def is_draw(self) -> bool:
        return self.winner is None and all(v is not None for v in self.board)

    def game_over(self) -> bool:
        return self.winner is not None or self.is_draw()

    def clone(self) -> "TicTacToe":
        clone = TicTacToe(self.current_player)
        clone.board = self.board.copy()
        clone.winner = self.winner
        return clone

    def pretty_board(self) -> str:
        def cell(i):
            return self.board[i] if self.board[i] is not None else str(i)
        rows = [f" {cell(0)} | {cell(1)} | {cell(2)} ",
                f" {cell(3)} | {cell(4)} | {cell(5)} ",
                f" {cell(6)} | {cell(7)} | {cell(8)} "]
        return "\n-----------\n".join(rows)

    def reset(self, starting_player: str = "X") -> None:
        self.__init__(starting_player=starting_player)

if __name__ == "__main__":
    # Simple manual smoke test
    g = TicTacToe()
    print(g.pretty_board())
    g.make_move(0)
    g.make_move(4)
    g.make_move(1)
    g.make_move(8)
    g.make_move(2)  # X wins
    print(g.pretty_board())
    print("Winner:", g.winner)
