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
        print(f"This is evaluation {evaluation_function(game, 'X')}")
        if ai_player and game.current_player == ai_player:
            move = best_move(game, ai_player) if optimal else random_move(game)
            print(f"AI ({ai_player}) chooses {move}")
            game.make_move(move)
            print(f"This is evaluation for ai {evaluation_function(game, ai_player)}")

        else:

            try:
                raw = input(f"Player {game.current_player} enter move (0-8): ").strip()
                move = int(raw)
            except ValueError:
                print("Invalid input. Enter a digit 0-8.")
                continue
            else:
                if not game.make_move(move):
                    print("Invalid move. Try again.")
            
    print("\nFinal board:")
    print(f"This is evaluation {evaluation_function(game, ai_player)}")

    print(game.pretty_board())
    __who_won(game)

def __who_won(game):
    if game.winner:
        print(f"Winner: {game.winner}")
    else:
        print("It's a draw!")

def evaluation_function(game_state: TicTacToe, player: str) -> float:
    """Evaluate the game state for the given player.

    Args:
        game_state: Current board state.
        player: 'X' or 'O'.
    Returns:
        A float score representing the favorability of the state for the player.
    """
    evaluation = 0.0
    opponent = 'O' if player == 'X' else 'X'

    # Terminal state evaluation
    if game_state.winner == player:
        evaluation += 1.0 # Win
    elif game_state.winner == opponent:
        evaluation -= 1.0   # Loss
    elif game_state.game_over() and game_state.winner is None:
        evaluation += 0.0  # Draw
    else:
        #Non-terminal state evaluation
        if game_state.board[4] == player:
            evaluation += 0.1  # Center control
        elif game_state.board[4] == opponent:
            evaluation -= 0.1  # Opponent center control
        for i in [0, 2, 6, 8]:
            if game_state.board[i] == player:
                evaluation += 0.05  # Corner control
            elif game_state.board[i] == opponent:
                evaluation -= 0.05  # Opponent corner control
        # Adjacent cells
        adjacent_indices = [(0,1), (1,2), (3,4), (4,5), (6,7), (7,8),
                            (0,3), (3,6), (1,4), (4,7), (2,5), (5,8),
                            (2,4), (4,6), (0,4), (4,8)]
        
        for i, j in adjacent_indices:
            if game_state.board[i] == player and game_state.board[j] == player:
                evaluation += 0.03  # Adjacent control
            elif game_state.board[i] == opponent and game_state.board[j] == opponent:
                evaluation -= 0.03  # Opponent adjacent control

    return evaluation
    

    


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Play Tic Tac Toe in the terminal")
    parser.add_argument("--ai", action="store_true", help="Play against an AI (you are X, AI is O)")
    parser.add_argument("--random", action="store_true", help="When used with --ai, AI plays randomly instead of optimally")
    args = parser.parse_args(argv)
    play(vs_ai=args.ai, optimal=not args.random)

if __name__ == "__main__":
    main()
