#!/usr/bin/python3
"""
N Queens puzzle solver.
"""

import sys


def print_solution(board):
    """Prints the board with queens' positions in the required format."""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def is_safe(board, row, col):
    """
    Checks if a queen can be placed on board[row][col].

    Args:
        row: The row index to check.
        col: The column index to check.

    Returns:
        bool: True if it is safe to place the queen, False otherwise.
    """
    for i in range(row):
        # Check the same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Solves the N Queens problem using backtracking.

    Args:
        board: The current state of the board.
        row: The current row to place a queen.
        n: The size of the board (n x n).
    """
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            # Backtrack


def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board (list of size N)
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
