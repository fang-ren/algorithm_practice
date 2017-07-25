"""
author: fangren
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        output = [0] * len(nums)
        if zero_count == 1:
            index_zero = nums.index(0)
            product = 1
            for i in nums:
                if i != 0:
                    product *= i
            output[index_zero] = product
        else:
            first_product = 1
            for i in nums[1:]:
                first_product *= i
            output[0] = first_product
            current_product = first_product
            for i in range(1, len(nums)):
                current_product = current_product/nums[i]*nums[i-1]
                output[i] = current_product
        return output


solution = Solution()
nums = [1,2,3,4]
print solution.productExceptSelf(nums)