"""
author: fangren
"""
class Solution(object):
    def all_permu(self, A):
        if len(A) <= 1:
            return [A]
        else:
            ans = []
            sub_permu = self.all_permu(A[1:])
            for elem in sub_permu:
                for i in range(len(A)):
                    ans.append(elem[:i] + [A[0]] + elem[i:])
            return ans

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = range(1, N+1)
        permutations = self.all_permu(N)
        beautiful_arrangements = []
        for arrangement in permutations:
            beautiful = True
            for i in range(1, len(arrangement)+1):
                if arrangement[i-1] % i == 0 or i % arrangement[i-1] == 0:
                    pass
                else:
                    beautiful = False
                    break
            #print i
            if beautiful == True:
                beautiful_arrangements.append(arrangement)
        return len(beautiful_arrangements)

solution = Solution()
print solution.countArrangement(10)
