# Stone Paper Scissors

A simple command-line **Stone Paper Scissors** game built with Python.

The project uses basic object-oriented programming, random computer moves, user input, game logic, and score tracking.

## Features

- Play Stone Paper Scissors against the computer
- Computer generates a random move for every round
- Tracks the user's and computer's scores
- Handles invalid inputs
- Type `quit` to stop the game
- Displays the final score when the game ends

## Concepts Used

- Python classes and objects
- `random.choice()`
- Conditional statements
- Loops
- Functions and methods
- User input handling
- Basic game-state management

## Project Structure

```text
stone-paper-scissors/
│
├── README.md
├── stone_paper_scissors.py
├── requirements.txt
├── .gitignore
└── notebooks/
    └── stone_paper_scissors.ipynb
```

No external Python packages are required.

## How to Play

Enter one of:

```text
stone
paper
scissors
```

To exit:

```text
quit
```

The computer chooses its move randomly, and the winner is determined using the standard rules:

- Stone beats scissors
- Scissors beats paper
- Paper beats stone

## Example

```text
=== Stone Paper Scissors ===
Choose stone, paper, or scissors (or type 'quit' to exit): stone
Computer chose: scissors
You win!

Score → You: 1 | Computer: 0
```

## Learning Objective

This project was created to practice Python fundamentals and apply object-oriented programming concepts to a small interactive application.
