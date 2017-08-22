"""
8/20/2017
Author: Fang Ren
"""

"""
You have a array with integers:

[ 1, -2, 0, 6, 2, -4, 6, 6 ]
You need to write a function which will evenly return indexes of a max value in the array. 
In the example below max value is 6, and its positions are 3, 6 and 7. So each run function should return random index from the set. 

Try to implement with O(n) for computation and memory. 
Try to reduce memory complexity to O(1).

"""

# the solution is not even. It's weighed by the number of elements in between
import random
def evenMax(A):
    length = len(A)
    start = random.randrange(length)
    max = start
    for i in range(1, length):
        if A[(i+start)%length] > A[max]:
            max = (i+start)%length
    return max

A = [1, -2, 0, 6, 2, -4, 6, 6 ]
maxes = []

for i in range(1000):
    max = evenMax(A)
    print max
    maxes.append(max)
import matplotlib.pylab as plt
plt.hist(maxes, bins = 100)
plt.show()
