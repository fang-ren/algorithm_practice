"""
author: fangren

8/3/2017
"""

class Solution(object):
    def findLongestChains(self, pairs):
        if len(pairs) <= 1:
            return pairs
        first_pair = pairs[0]
        rest_pairs = pairs[1:]
        rest_chain = self.findLongestChains(rest_pairs)
        if rest_chain[0][0] > first_pair[1]:
            return [first_pair] + rest_chain
        else:
            return rest_chain

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs)
        chains = self.findLongestChains(pairs)
        return len(chains)


solution = Solution()
print solution.findLongestChains([[1,2],[2,3],[3,4]])