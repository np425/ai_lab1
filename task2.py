"""
Task 2.
- Create 2d array with 5 rows and 3 columns
- Stores student names
- Stores student last names
- Stores student grades
"""

from typing import List
import numpy as np
from numpy import random

def _rand_file_lines(file_name: str, amount: int) -> np.ndarray:
    lines = []
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return random.choice(lines, size=amount)

def first_names(amount: int) -> np.ndarray:
    return _rand_file_lines('first_names.txt', amount)

def last_names(amount: int) -> np.ndarray:
    return _rand_file_lines('last_names.txt', amount)

def grades(amount: int) -> np.ndarray:
    return random.randint(1, 10, size=amount)

ROWS = 5

data = np.column_stack((first_names(ROWS), last_names(ROWS), grades(ROWS)))
