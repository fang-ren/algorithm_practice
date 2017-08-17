"""
8/16/2017
Author: Fang Ren
"""

"""
Find the common elements of two sorted array. If one array is small, the other is very big

"""

def binarySearch(A, elem):
    # find the largest number in A that is no larger than "elem"
    length = len(A)
    if length == 1:
        return 0
    middle = length/2
    if elem < A[middle]:
        return binarySearch(A[:middle], elem)
    else:
        return middle + binarySearch(A[middle:], elem)

# A = [1,1.9, 3,4,5,6,7]
# elem = 4
# print binarySearch(A, elem)

def commonElements(A, B):
    # A is large array, B is the small array
    common = []
    for elem in B:
        elem_in_A = binarySearch(A, elem)
        if A[elem_in_A] == elem:
            common.append(elem)
        A = A[elem_in_A:]
    return common

A = range(100)
B = [-2,4,6]
print commonElements(A, B)