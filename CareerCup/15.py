"""
author: Fang Ren (SSRL)

9/5/2017
"""

"""
Push all the zero's of a given array to the end of the array. In place only. Ex 1,2,0,4,0,0,8 becomes 1,2,4,8,0,0,0
- CheckThisResume.com March 09, 2012 in United States | Report Duplicate | Flag 
"""

import numpy as np

def pushingZeros(A):
    B = np.zeros_like(A)
    begin_index = 0
    for elem in A:
        if elem != 0:
            B[begin_index] = elem
            begin_index += 1
    return B

A = [1,2,0,4,0,0,8]
print pushingZeros(A)