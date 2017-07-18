"""
author: fangren
"""

import numpy as np
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        elems, count = np.unique(list(s), return_counts= True)
        ans = ''
        for elem, c in zip(elems, count):
            #print type(elem), type(c)
            ans += str(elem) * int(c)
        return ans

solution = Solution()
print solution.frequencySort('tree')