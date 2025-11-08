# Tic Tac Toe (Python)

A simple, test-backed Tic Tac Toe game with:
- Core game logic (`tictactoe.game.TicTacToe`)
- An optimal AI using minimax (`tictactoe.ai.best_move`)
- A terminal CLI (`python -m tictactoe.cli`)

## How to run

Play human vs human:

```bash
python -m tictactoe.cli
```

Play against the optimal AI (you are X, AI is O):

```bash
python -m tictactoe.cli --ai
```

Play against a random AI:

```bash
python -m tictactoe.cli --ai --random
```

## Development

Run unit tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Project layout:

```
Project/
├─ tictactoe/
│  ├─ __init__.py
│  ├─ game.py      # core logic
│  └─ ai.py        # minimax AI
├─ tests/
│  └─ test_game.py
└─ README.md
```

No external dependencies are required (standard library only).
