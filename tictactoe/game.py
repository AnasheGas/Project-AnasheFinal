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
        """Create a new TicTacToe game.

        Args:
            starting_player: 'X' or 'O' indicating who moves first.

        Initializes an empty board, sets the current player and clears any winner.
        """
        self.is_valid_player(starting_player)
        self.board: List[Optional[str]] = [None] * 9
        self.current_player: str = starting_player
        self.winner: Optional[str] = None

    def is_valid_player(self, starting_player):
        """Validate a player symbol.

        Args:
            starting_player: value to validate.

        Raises:
            ValueError: if starting_player is not 'X' or 'O'.
        """
        if starting_player not in ("X", "O"):
            raise ValueError("starting_player must be 'X' or 'O'")

    def available_moves(self) -> List[int]:
        """Return a list of available move indices.

        Returns:
            A list of integers (0-8) for empty board positions.
        """
        return [i for i, v in enumerate(self.board) if v is None]

    def make_move(self, position: int) -> bool:
        """Attempt to place the current player's mark at position.

        Args:
            position: board index (0-8) to place the mark.

        Returns:
            True if the move succeeds; False if the move is invalid or the game is finished.

        Side effects:
            Updates the board, winner state, and (if the game continues) switches current player.
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
        """Return True if the game is a draw.

        A draw is when all cells are filled and there is no winner.
        """
        return self.winner is None and all(v is not None for v in self.board)

    def game_over(self) -> bool:
        """Return True if the game has finished.

        The game is over when there is a winner or a draw.
        """
        return self.winner is not None or self.is_draw()

    def clone(self) -> "TicTacToe":
        """Return a shallow copy of the game state.

        The returned instance has a copy of the board, the same current_player and winner.
        """
        clone = TicTacToe(self.current_player)
        clone.board = self.board.copy()
        clone.winner = self.winner
        return clone

    def pretty_board(self) -> str:
        """Return a human-readable string of the board.

        Empty cells are shown as their index number to aid move selection.
        """
        def cell(i):
            return self.board[i] if self.board[i] is not None else str(i)
        rows = [f" {cell(0)} | {cell(1)} | {cell(2)} ",
                f" {cell(3)} | {cell(4)} | {cell(5)} ",
                f" {cell(6)} | {cell(7)} | {cell(8)} "]
        return "\n-----------\n".join(rows)

    def reset(self, starting_player: str = "X") -> None:
        """Reset the game to an initial empty state.

        Args:
            starting_player: 'X' or 'O' to set as the next current player.
        """
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
