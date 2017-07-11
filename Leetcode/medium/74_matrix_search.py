"""
author: fangren
"""
# search a target value in a matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import numpy as np
        matrix = np.array(matrix)
        matrix = matrix.flatten()
        if len(matrix) == 0:
            return False
        elif len(matrix) == 1:
            if target == matrix[0]:
                return True
            else:
                return False
        elif len(matrix) > 1:
            left = matrix[:len(matrix)/2]
            right = matrix[len(matrix)/2:]
            print left, right
            if matrix[len(matrix)/2] <= target:
                return self.searchMatrix(right, target)
            else:
                return self.searchMatrix(left, target)