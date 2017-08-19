"""
8/17/2017
Author: Fang Ren
"""

"""
divide 2 numbers without using / or %
"""

def dividing(a, b):
    ans = 0
    if b == 0 and a != 0:
        return "Infinity"
    if a == 0:
        return 0
    if a*b > 0:
        sign = '+'
    elif a * b < 0:
        sign = '-'
    a = abs(a)
    b = abs(b)
    while a >= b:
        a = a-b
        ans += 1
    if sign == '+':
        return ans, a
    if sign == '-':
        return -ans, a

print dividing(11, -5), 11/(-5), 11%(-5)

