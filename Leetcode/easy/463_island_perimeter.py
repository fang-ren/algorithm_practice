"""
author: fangren
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        perim = 0
        row_num = len(grid)
        col_num = len(grid[0])
        for row in range(row_num):
            for col in range(col_num):
                elem = grid[row][col]
                if elem == 1:
                    if row-1 < 0:
                        perim += 1
                    if row-1 >= 0 and grid[row-1][col] == 0:
                        perim += 1
                    if row + 1 >= row_num:
                        perim += 1
                    if row + 1 < row_num and grid[row+1][col] == 0:
                        perim += 1
                    if col-1 < 0:
                        perim += 1
                    if col-1 >= 0 and grid[row][col-1] == 0:
                        perim += 1
                    if col + 1 >= col_num:
                        perim += 1
                    if col + 1 < col_num and grid[row][col+1] == 0:
                        perim += 1
        return perim

solution = Solution()
grid = [[0,1]]
print solution.islandPerimeter(grid)