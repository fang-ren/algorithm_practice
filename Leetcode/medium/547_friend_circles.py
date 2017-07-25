"""
author: fangren
"""

class Solution(object):
    def findCircle(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M == []:
            return []
        if M == [[1]]:
            return [[0]]
        current_circle = [len(M)-1] # circle that contains the last element 0
        M_sub = [i[:-1] for i in M[:-1]]
        #print M_sub
        #print current_circle, M_sub
        others_circles = self.findCircle(M_sub) # circles formed by all the other elements except the last element, list of list
        new_others_circles = others_circles[:]
        for circle in others_circles:
            for people in circle:
                if M[-1][people] == 1:
                    current_circle += circle
                    new_others_circles.remove(circle)
                    break
        new_others_circles.append(current_circle)
        return new_others_circles

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return len(self.findCircle(M))


solution = Solution()
M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# M = [[1,0],[0, 1]]
print solution.findCircle(M)
print solution.findCircleNum(M)

