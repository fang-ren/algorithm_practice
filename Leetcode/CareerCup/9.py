"""
8/19/2017
Author: Fang Ren
"""

"""
find famous person in a list of people
"""


def famousPerson(A):
    B = A[:]
    candidate = 0
    for i in range(1, len((A))):
        if isKnow(candidate, i):
            candidate = i
    famous = True
    if any(isknow(candidate, i) for i in xrange(candidate)):
        return -1
    if any(isKnow(candidate, person) for person in xrange(A)):
        return -1


