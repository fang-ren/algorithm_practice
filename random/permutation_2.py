"""
author: fangren
"""

def all_permu(A):
    if len(A) <= 1:
        return [A]
    else:
        ans = []
        sub_permu = all_permu(A[1:])
        for elem in sub_permu:
            for i in range(len(A)):
                ans.append(elem[:i] + [A[0]] + elem[i:])
        print ans
        return ans

A = [1,2,3]
print all_permu(A)