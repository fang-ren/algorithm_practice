"""
author: fangren
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        keys = dict.keys()
        values = dict.values()
        sorted_keys = [key for (value, key) in sorted(zip(values, keys), reverse= True)]
        return sorted_keys[:k]