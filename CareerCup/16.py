"""
author: Fang Ren (SSRL)

9/5/2017
"""

"""
A k-palindrome is a string which transforms into a palindrome on removing at most k characters.

Given a string S, and an interger K, print "YES" if S is a k-palindrome; otherwise print "NO".
Constraints:
S has at most 20,000 characters.
0<=k<=30

Sample Test Case#1:
Input - abxa 1
Output - YES
Sample Test Case#2:
Input - abdxa 1
Output - No

"""

def delete_distance(S):
    ans = 0
    if len(S) <=1:
        return 0
    elif S[0] == S[-1]:
        return delete_distance(S[1:-1])
    else:
        return 1+ min(delete_distance(S[1:]), delete_distance(S[:-1]))


def k_palindrome(S, K):
    ans = delete_distance(S)
    if ans <= K:
        print 'YES'
    else:
        print 'NO'

k_palindrome('abdefghzhilopqrstuvwxyzxaaxzyxwvutsrqpolihzhgfedba', 1)