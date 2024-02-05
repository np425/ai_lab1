"""
Task 1.
- Create 1d array with 10 random numbers from 0 to 100 
- Calculate sum
- Calculate average
- Calculate standard deviation
"""

import numpy as np
from numpy import random

arr = random.randint(100, size=10)

sum = np.sum(arr)
average = np.average(arr)
deviation = np.std(arr)

print('Array:',arr)

print('Sum:',sum)
print('Average:',average)
print('Standard Deviation:',deviation)

