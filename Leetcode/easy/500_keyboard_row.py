"""
author: Fang Ren (SSRL)

7/10/2017
"""


class Solution():
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('QWERTYUIOP')
        row2 = set('ASDFGHJKL')
        row3 = set('ZXCVBNM')
        ans = []
        for word in words:
            w = set(word.upper())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                ans.append(word)
        return ans



words = ["Hello","Alaska","Dad","Peace"]
solution = Solution()
ans = solution.findWords(words)
print ans