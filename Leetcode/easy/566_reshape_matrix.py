"""
author: Fang Ren (SSRL)

7/10/2017
"""


class Solution():
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums == []:
            return nums
        new_nums = [[None]*c for x in xrange(r)]
        if type(nums[0]) == int:
            if len(nums) != r*c:
                return nums
            else:
                for i in range(len(nums)):
                    #print i/c, i%c, nums[i]
                    new_nums[i/c][i%c] = nums[i]
                    #print new_nums[i/c][i%c], new_nums
        elif type(nums[0]) != int:
            if len(nums) * len(nums[0]) != r*c:
                return nums
            else:
                for i in range(len(nums)):
                    for j in range(len(nums[i])):
                        print i, j, len(nums)
                        #print (i * len(nums) + j) / c, (i * len(nums) + j) % c, nums[i][j]
                        new_nums[(i*len(nums[0])+j)/c][(i*len(nums[0])+j) % c] = nums[i][j]
        return new_nums


solution = Solution()
nums = [[1,2,3],[4,5,6]]
# nums = []
# nums = [1,2,3,4,5,6]
print solution.matrixReshape(nums, 3, 2)