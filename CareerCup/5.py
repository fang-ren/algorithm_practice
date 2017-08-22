"""
8/17/2017
Author: Fang Ren
"""

"""
find the point which has the maximum overlap of the intervals

Consider a big party where a log register for guests entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.

Example:

Input: arrl = [1, 2, 9, 5, 5]
       exit = [4, 5, 12, 9, 12]
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5

"""

#
# def overlap(arrl, exit):
#     log = sorted(zip(arrl, exit))
#     new_log = log[:]
#     points_to_check = set(arrl + exit)
#     overlapping = []
#     for point in points_to_check:
#         overlapping.append(0)
#         for guest in log:
#             #print guest, point
#             if guest[0] <= point and guest[1] >= point:
#                 overlapping[-1] += 1
#             if guest[1] < point:
#                 new_log.remove(guest)
#                 print log, new_log
#         log = new_log[:]
#     return max(overlapping)

# a more efficient method

def overlap(arrl, exit):
    arrl = [[a, 'a'] for a in arrl]
    exit = [[e, 'e'] for e in exit]
    events = sorted(arrl + exit)
    overlappings = []
    overlapping = 0
    for event in events:
        if event[1] == 'a':
            overlapping += 1
        elif event[1] == 'e':
            overlapping -= 1
        overlappings.append(overlapping)
    return max(overlappings)



arrl = [1, 2, 9, 5, 5]
exit = [4, 5, 12, 9, 12]
print overlap(arrl, exit)
