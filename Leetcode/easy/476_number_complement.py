class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:]
        ans = ''
        for i in num:
            ans += 1-i
        return int(ans,2)

