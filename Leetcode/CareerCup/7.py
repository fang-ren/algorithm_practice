"""
8/18/2017
Author: Fang Ren
"""

"""
find the length of the longest arithmetic progression in array
"""

import numpy as np

def longestArithmetic(A):
    differences = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            differences.append((A[j]-A[i]))
    return max(np.unique(differences, return_counts=True)[1])

A = [1, 7, 10, 15, 27, 29]
B = [5, 10, 15, 20, 25, 30]

print longestArithmetic(A)

