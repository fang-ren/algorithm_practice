"""
author: Fang Ren (SSRL)

9/5/2017
"""

"""
WAP to modify the array such that arr[I] = arr[arr[I]].
Do this in place i.e. without using additional memory.

example : if a = {2,3,1,0}
o/p = a = {1,0,3,2}

Note : The array contains 0 to n-1 integers.

"""

import numpy as np

a = np.array([2,3,1,0])
#print a[a]

print [a[i] for i in a]