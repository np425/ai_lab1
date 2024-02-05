"""
Task 4.
- From 2nd task array calculate grades average and standard deviation
"""

import numpy as np
from task2 import data

print('Original rows:')
print(data)

grades = data[:,2].astype(int)
average = np.average(grades)
deviation = np.std(grades)

print("Grades:", grades)
print("Average grades:", average)
print("Standard deviation of grades:", deviation)
