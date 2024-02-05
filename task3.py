"""
Task 3.
- From 2nd task array filter out students whose grade is higher than 8
"""

import numpy as np
from task2 import data

MIN_GRADE = 8

print('Original rows:')
print(data)

filtered_rows = data[data[:,2].astype(int) > MIN_GRADE]
print('Filtered rows:')
print(filtered_rows)

filtered_students = filtered_rows[:,0]
print('Filtered students:')
print(filtered_students)
