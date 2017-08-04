"""
author: Fang Ren (SSRL)

"""

def insert_sort(A):
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

def merge_sort(A):
    length = len(A)
    if length <= 1:
        return A
    if length == 2:
        if A[0] < A[1]:
            A[0], A[1] = A[1], A[0]
        return A
    left = merge_sort(A[:length/2])
    right = merge_sort(A[length/2:])
    sorted = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted = sorted + left[i:] + right[j:]
    return sorted

A = [1,2,3,4]
print insert_sort(A)
print merge_sort(A)

