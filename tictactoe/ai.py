from __future__ import annotations
import math
import random
from typing import Tuple
from .game import TicTacToe

def random_move(game: TicTacToe) -> int:
    return random.choice(game.available_moves())

def best_move(game: TicTacToe, player: str) -> int:
    """Return optimal move for player using minimax with alpha-beta pruning."""
    assert player in ("X", "O")
    best_score = -math.inf
    move_choice = None
    for move in game.available_moves():
        clone = game.clone()
        clone.current_player = player
        clone.make_move(move)
        score = _minimax(clone, player, maximizing=False, alpha=-math.inf, beta=math.inf)
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice if move_choice is not None else random_move(game)

def _utility(game: TicTacToe, player: str) -> int:
    opponent = "O" if player == "X" else "X"
    if game.winner == player:
        return 1
    if game.winner == opponent:
        return -1
    return 0  # draw or ongoing

# def _minimax(game: TicTacToe, player: str, maximizing: bool, alpha: float, beta: float) -> int:
#     if game.game_over():
#         return _utility(game, player)
#     current_player = game.current_player
#     opponent = "O" if current_player == "X" else "X"

#     if maximizing:
#         value = -math.inf
#         for move in game.available_moves():
#             clone = game.clone()
#             clone.current_player = current_player
#             clone.make_move(move)
#             value = max(value, _minimax(clone, player, maximizing=False, alpha=alpha, beta=beta))
#             alpha = max(alpha, value)
#             if beta <= alpha:
#                 break
#         return value
#     else:
#         value = math.inf
#         for move in game.available_moves():
#             clone = game.clone()
#             clone.current_player = current_player
#             clone.make_move(move)
#             value = min(value, _minimax(clone, player, maximizing=True, alpha=alpha, beta=beta))
#             beta = min(beta, value)
#             if beta <= alpha:
#                 break
#         return value

def _mini_max_value(given_game: TicTacToe, player: str, value, alpha, beta) -> int:
    """Return the minimax value of the game state for the given player."""

    maximizing = (value == -math.inf)

    # for move in given_game.available_moves():
    #     clone = given_game.clone()
    #     clone.make_move(move)

    #     score = _minimax(clone, player, maximizing=not maximizing,alpha=alpha,beta=beta)

    #     # Unified update
    #     value = (max if maximizing else min)(value, score)

    #     # Update alpha/beta
    #     if maximizing:
    #         alpha = max(alpha, value)
    #     else:
    #         beta = min(beta, value)

    #     # Pruning
    #     if beta <= alpha:
    #         break


    for move in given_game.available_moves():
        clone = given_game.clone()
        clone.make_move(move)

        score = _minimax(clone, player, maximizing=not maximizing,alpha=alpha,beta=beta)

        # Unified update
        value = (max if maximizing else min)(value, score)

        # Update alpha/beta
        if maximizing:
            alpha = max(alpha, value)
        else:
            beta = min(beta, value)

        # Pruning
        if beta <= alpha:
            break

    return value


def _minimax(game: TicTacToe, player: str, maximizing: bool, alpha: float, beta: float) -> int:
    if game.game_over():
        return _utility(game, player)
    current_player = game.current_player
    opponent = "O" if current_player == "X" else "X"
    value = 0
    if maximizing:
        value = -math.inf
        return _mini_max_value(game, player, value, alpha, beta)
    else:
        value = math.inf
        return _mini_max_value(game, player, value, alpha, beta)
    



__all__ = ["random_move", "best_move"]
