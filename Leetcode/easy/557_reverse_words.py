"""
author: Fang Ren (SSRL)

7/10/2017
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split()
        new_list = []
        for word in list:
            word = word[::-1]
            new_list.append(word)
        new_word = ' '.join(new_list)
        return new_word
