"""
8/20/2017
Author: Fang Ren
"""
"""
The number of valid combinations of a strings for given input array a[], where a=>1, z => 26, and 0 <= a[i] <= 9 

{1,1,1} => {aaa, ak, ka} => 3 
{1,1,0} => {aj} => 1
"""

def validCombination(A):
    if len(A) == 0:
        return []
    if len(A) == 1:
        return [A]
    last_letter = A[-1]
    rest_combination = validCombination(A)
    for combination in rest_combination:
        if combination[-1]:




A = [1,1,0]
print validCombination(A)
