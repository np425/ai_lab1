"""
Task 5.
- Create 2d 8x8 array consisting of alternating values between 0,1 representing a chess board
- Filter out black squares (1) from the center 4x4 area
"""

import numpy as np

ROWS = 8
COLS = 8

board = np.fromfunction(lambda i, j: (i+j)%2, (ROWS,COLS), dtype=int)
print("Board:")
print(board)

MID_ROW = ROWS//2
MID_COL = COLS//2

middle = board[MID_ROW - 2:MID_ROW + 2, MID_COL - 2:MID_COL + 2]
print("Middle:")
print(middle)

