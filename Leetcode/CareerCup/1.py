"""
8/16/2017
Author: Fang Ren
"""

"""
Given a sorted array A, find how many subsets of A satisfies MIN(subset) + MAX(subset) < K.
"""
def subsetCount(index_of_max, index_of_min):
    if index_of_max == index_of_min:
        return 1
    return 2**(index_of_max-index_of_min-1)

def findSubsets(A, K):
    ans = 0
    for i in range(len(A)-1, -1, -1):
        max = A[i]
        if max * 2 < K:
            j = i
        else:
            j = i - 1
            while (A[j] + max) >= K and j >= 0:
                # better to use binary search here
                j = j-1
        while j >= 0:
            ans += subsetCount(i, j)
            j = j-1
    return ans

A = [1,2,3,4,5]
K = 6
print findSubsets(A, K)
