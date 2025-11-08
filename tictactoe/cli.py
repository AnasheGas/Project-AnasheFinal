from __future__ import annotations
import argparse
from typing import Optional
from .game import TicTacToe
from .ai import random_move, best_move

def play(vs_ai: bool = False, optimal: bool = True) -> None:
    game = TicTacToe()
    ai_player = "O" if vs_ai else None
    print("Tic Tac Toe — indices shown for empty cells")
    while not game.game_over():
        print("\nCurrent board:")
        print(game.pretty_board())
        if ai_player and game.current_player == ai_player:
            move = best_move(game, ai_player) if optimal else random_move(game)
            print(f"AI ({ai_player}) chooses {move}")
            game.make_move(move)
            continue
        try:
            raw = input(f"Player {game.current_player} enter move (0-8): ").strip()
            move = int(raw)
        except ValueError:
            print("Invalid input. Enter a digit 0-8.")
            continue
        if not game.make_move(move):
            print("Invalid move. Try again.")
    print("\nFinal board:")
    print(game.pretty_board())
    if game.winner:
        print(f"Winner: {game.winner}")
    else:
        print("It's a draw!")


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Play Tic Tac Toe in the terminal")
    parser.add_argument("--ai", action="store_true", help="Play against an AI (you are X, AI is O)")
    parser.add_argument("--random", action="store_true", help="When used with --ai, AI plays randomly instead of optimally")
    args = parser.parse_args(argv)
    play(vs_ai=args.ai, optimal=not args.random)

if __name__ == "__main__":
    main()
