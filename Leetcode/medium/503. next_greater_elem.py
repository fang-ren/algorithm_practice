class Solution(object):
    def returnIndex(self, index, nums_length):
        if index >= 0 and index < nums_length:
            return index
        elif index <0:
            return index + nums_length
        else:
            return index - nums_length

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # handle first element in the nums
        if max(nums) == nums[0]:
            ans = [-1]
            while
                ans.append()
        else:
            while
                ans.append()


        nums_length = len(nums)
        i = len(ans)
        while len(ans) < nums_length:
            if nums[i] <= nums[self.returnIndex(i - 1, nums_length)]:
                ans.append(ans[-1])
            else:
                searched = 1
                while searched <= nums_length:
                    if nums[self.returnIndex(i+searched, nums_length)] >= num:
                        ans.append(nums[self.returnIndex(i+searched, nums_length)])
                    else:
                        searched += 1

        return ans

