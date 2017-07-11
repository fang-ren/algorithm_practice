"""
author: fangren
"""
A = ['a,', 'b', 'c', 'd', 'e', 'f']
A = [1, 2, 3]

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

permutation_list = []
for i in all_perms(A):
    permutation_list.append(i)

print permutation_list