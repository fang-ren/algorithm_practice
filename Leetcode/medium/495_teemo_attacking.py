"""
author: fangren
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        if len(timeSeries) == 1:
            return duration
        poisoinedTime = 0
        for i in range(1, len(timeSeries)):
            end = timeSeries[i-1] + duration
            if timeSeries[i] > end:
                poisoinedTime += duration
            else:
                poisoinedTime += (timeSeries[i] - timeSeries[i - 1])
        poisoinedTime += duration
        return poisoinedTime



solution = Solution()
timeSeries = [1]
duration = 100000
print solution.findPoisonedDuration(timeSeries, duration)

