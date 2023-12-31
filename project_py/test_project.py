# test_project.py
from project import evaluate, wins, game_over

def test_evaluate_win():
    """
    Test evaluate function for a winning condition.
    """
    # Example board where COMP has won
    board = [
        [+1, +1, +1],
        [0, -1, -1],
        [0, 0, 0]
    ]
    assert evaluate(board) == +1

def test_evaluate_loss():
    """
    Test evaluate function for a losing condition.
    """
    # Example board where HUMAN has won
    board = [
        [-1, -1, -1],
        [0, +1, +1],
        [0, 0, 0]
    ]
    assert evaluate(board) == -1

def test_evaluate_draw():
    """
    Test evaluate function for a draw condition.
    """
    # Example board for a draw
    board = [
        [+1, -1, +1],
        [-1, -1, +1],
        [+1, +1, -1]
    ]
    assert evaluate(board) == 0

def test_wins():
    """
    Test wins function for various win conditions.
    """
    board = [
        [+1, +1, +1],
        [0, -1, -1],
        [0, 0, 0]
    ]
    assert wins(board, +1)

    board = [
        [-1, 0, 0],
        [-1, +1, +1],
        [-1, 0, 0]
    ]
    assert wins(board, -1)

    board = [
        [+1, -1, 0],
        [0, +1, -1],
        [-1, 0, +1]
    ]
    assert not wins(board, +1)

def test_game_over():
    """
    Test game_over function for various game states.
    """
    board = [
        [+1, +1, +1],
        [0, -1, -1],
        [0, 0, 0]
    ]
    assert game_over(board)

    board = [
        [-1, -1, -1],
        [0, +1, +1],
        [0, 0, 0]
    ]
    assert game_over(board)

    board = [
        [+1, -1, +1],
        [-1, -1, +1],
        [+1, +1, -1]
    ]
    assert game_over(board)

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert not game_over(board)
