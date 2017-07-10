
def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums, reverse= True)
    print nums
    result = sum(nums[i] for i in range(len(nums)) if i%2 == 1)
    return result



a = arrayPairSum([1,4,3,2])
