"""
author: fangren
"""

Q: given an array of positive integers. Return the length of the longest sub-sequence whose sum add up to K, where K is a positive integer. Return -1 if nothing is found.

ex:
Nums = 1,10,  5, 5, 5, 2, 3

K = 15

5,5,2,3
Ans = 4

Import numpy as np
Def sub_sequence(nums, K):
	If sum(nums) < K:
		Return -1
	If len(nums) == 0:
		Return -1
Sub_sum = 0
Sub_sums = []
for num in nums:
	Sub_sum += num
	sub_sums.append(sub_sum)
Sub_sums = np.array(sub_sums)
0# 1,10,  5, 5, 5, 2, 3
1# 1, 11, 16, 21, 26,  28, 31
10# 0, 10, 15, 20, 25, 27, 30
5# -10, 0, 5, 10, 15, 17, 20
5# -15, -5, 0, 5, 10, 12, 15
5# -20, -10,
Lengths = []
Start = 0
	While start < length(nums):
		If K in sub_sums:
			lengths.append(sub_sums.index(K)-start+1)
Sub_sums = sub_sums - nums[start]
Print Sub_sums
Start += 1
	Return max(lengths)





Def sub_sequence(nums, K):
	If len(nums) == 0:
		Return -1
Sub_sum = 0
Sub_sums = []
for num in nums:
	Sub_sum += num
	sub_sums.append(sub_sum)
Sub_sums = np.array(sub_sums)
# 1,10,  5, -6, 6, 5, 5, 2, 3
# 1, 11, 16, 10, 16,

Lengths = []
Start = 0
	While start < length(nums):
		If K in sub_sums:
			lengths.append(len(nums) -sub_sums[::-1].index(K)-start+1)
Sub_sums = sub_sums - nums[start]
Print Sub_sums
Start += 1
	Return max(lengths)

