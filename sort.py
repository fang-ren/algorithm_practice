"""
author: Fang Ren (SSRL)

3/13/2017
"""

"""
algorithm considers performance, resource, correctness, robustness
security, user friendliness

comparison sorting examples:
- quick sort n*log(n)
- merge sort n*log(n)
- insertion sort n**2
- heapsort n*log(n)
- bubble sort n**2

integer sorting examples:
- counting sort n
-
"""

# test case
a = [5,2,3,5,2,57,23, 4,52,100, 20, 1]

def insertion_sort(a):
    # sort in asc order
    if a[0] < a[1]:
        pass
    else:
        temp = a[0]
        a[0] = a[1]
        a[1] = temp
    # print a
    for i in range(2, len(a)):
        for j in range(1, i):
            if a[i] < a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            else:
                pass
    return a

# a = insertion_sort(a)
# print a

def merge_sort(a):
    # sort in asc order
    if len(a) <= 1:
        pass
    elif len(a) == 2:
        print 'comparing', a[0], a[1]
        if a[0] < a[1]:
            pass
        else:
            temp = a[0]
            a[0] = a[1]
            a[1] = temp
    else:
        LEFT = merge_sort(a[:len(a)/2])
        RIGHT = merge_sort(a[len(a)/2:])
        sorted = []
        l = 0
        r = 0
        print 'merging', LEFT, RIGHT
        while l < len(LEFT) and r < len(RIGHT):
            if LEFT[l] < RIGHT[r]:
                sorted.append(LEFT[l])
                l += 1
            else:
                sorted.append(RIGHT[r])
                r += 1
            #print sorted
        if l == len(LEFT):
            sorted += RIGHT[r:]
        else:
            sorted += LEFT[l:]
        a = sorted
    return a

a = merge_sort(a)
print a

# integer sorting
def counting_sort(a):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    for element in a:
        count[a] += 1
