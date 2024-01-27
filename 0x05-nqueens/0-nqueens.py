#!/usr/bin/python3
import sys

"""Solves the N queens problem: The N queens puzzle is the challenge of
   placing N non-attacking queens on an N×N chessboard.
"""


def print_board(chess_board, n):
    """print solution positions"""
    sol = []
    for r in range(n):
        for c in range(n):
            if chess_board[r][c] == 1:
                sol.append([r, c])
    print(sol)


def is_safe(chess_board, r, c, n):
    """Check if there is no queens on the current row, column or diagonal"""
    # column check
    for i in range(n):
        if chess_board[i][c]:
            return False

    # row check
    for i in range(n):
        if chess_board[r][i]:
            return False

    # two diagonals
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if chess_board[i][j]:
            return False

    for i, j in zip(range(r, -1, -1), range(c, n)):
        if chess_board[i][j]:
            return False

    return True


def n_queen_solution(chess_board, r, n):
    """use recursion to solve n queens problem"""
    if r == n:
        print_board(chess_board, n)
    else:
        for c in range(n):
            if is_safe(chess_board, r, c, n):
                chess_board[r][c] = 1
                n_queen_solution(chess_board, r + 1, n)
                chess_board[r][c] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    chess_board = [[0 for _ in range(n)] for _ in range(n)]
    n_queen_solution(chess_board, 0, n)
