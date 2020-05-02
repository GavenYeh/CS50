"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    X_count = 0
    O_count = 0
    for row in board:
        X_count += sum(1 for spot in row if spot == X)
        O_count += sum(1 for spot in row if spot == O)
    if X_count == O_count:
        return X
    elif X_count - O_count == 1:
        return O


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
    if board[action[0]][action[1]] != EMPTY:
        raise Exception('({}, {}) is not a valid option'
                        .format(action[0], action[1]))
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    win_board = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]
            ]

    if [X, X, X] in win_board:
        return X
    if [O, O, O] in win_board:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return ((not any(EMPTY in row for row in board)) or (winner(board) == X)
            or (winner(board) == 0))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def MAX(board):

        if terminal(board):
            return utility(board)

        v = -math.inf

        for action in actions(board):
            v = max(v, MIN(result(board, action)))
        return v            
            
    def MIN(board):

        if terminal(board):
            return utility(board)

        v = math.inf

        for action in actions(board):
            v = min(v, MAX(result(board, action)))
        return v            

    if board == initial_state():
        i, j = random.randint(0, 2), random.randint(0, 2)
        return (i, j)
    
    if player(board) == X:
        v = -math.inf
        move = (1,1)
        for action in actions(board):
            minv = MIN(result(board,action))
            if minv > v:
                v = minv
                move = action
        return move
    
    if player(board) == O:
        v = math.inf
        move = (1,1)
        for action in actions(board):
            maxv = MAX(result(board,action))
            if maxv < v:
                v = maxv
                move = action
        return move
                
                
        
