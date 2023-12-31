Tic-Tac-Toe AI
Video Demo:
Description:https://youtu.be/GxvLY7-p0Ak
This project is an implementation of a Tic-Tac-Toe game in Python, featuring an AI opponent that uses the minimax algorithm to calculate its moves. The goal was to create a simple yet challenging game that can be played in a console environment.

Files in the Project:

project.py: This is the main file that runs the Tic-Tac-Toe game. It includes the game's logic, AI implementation using the minimax algorithm, and user interaction. The game allows a player to play Tic-Tac-Toe against an AI opponent.

evaluate(state): Evaluates the game board to determine if a player has won.
wins(state, player): Checks if a specific player has won.
game_over(state): Determines if the game has ended.
Other utility functions assist in the game flow and AI decision-making.
test_project.py: Contains unit tests for several functions in project.py. It ensures the reliability of the functions evaluate, wins, and game_over.

test_evaluate_win(), test_evaluate_loss(), test_evaluate_draw(): Test cases for different outcomes in the evaluate function.
test_wins(): Tests the wins function for various win conditions.
test_game_over(): Tests the game_over function for different game states.
Design Choices:

Minimax Algorithm: Chosen for its effectiveness in turn-based games like Tic-Tac-Toe where it can forecast outcomes based on current game state.

Console-based Interface: To keep the project simple and focused on the AI logic, a console-based interface was chosen. It's user-friendly and straightforward, allowing focus on gameplay.

Modular Function Design: Functions were designed to be independent and reusable, allowing easier testing and potential future expansion, like implementing different game modes or AI algorithms.

This project not only serves as an entertaining game but also as a demonstration of AI implementation in a simple, well-known game context.
