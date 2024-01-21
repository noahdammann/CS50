"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if terminal(board):
        return None
    
    if board == initial_state():
        return X
    
    num_x = 0
    num_o = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1

    if (num_x > num_o):
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i_val = action[0]
    j_val = action[1]

    # Create a new board by creating a new list for each row
    new_board = [row[:] for row in board]

    new_board[i_val][j_val] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    p = 0
    while p < 3:
        if board[p][0] == board[p][1] == board[p][2] != EMPTY:
            return board[p][0]
        p += 1
    
    # Check columns
    q = 0
    while q < 3:
        if board[0][q] == board[1][q] == board[2][q] != EMPTY:
            return board[0][q]
        q += 1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY: 
        return board[1][1]

    # Return none
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check for winner
    if winner(board):
        return True
    
    # Check for full board
    empty_count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_count += 1

    if empty_count == 0:
        return True
    
    # Otherwise return false
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winPlayer = winner(board)
    if winPlayer == X:
        return 1
    elif winPlayer == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        val, move = max_value(board)
        return move
    else:
        val, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None
    for action in actions(board):
        new_v, mv = min_value(result(board, action))
        if new_v > v:
            v = new_v
            best_move = action
    return v, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None
    for action in actions(board):
        new_v, mv = max_value(result(board, action))
        if new_v < v:
            v = new_v
            best_move = action
    return v, best_move