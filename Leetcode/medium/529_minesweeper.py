"""
author: fangren
"""

class Solution(object):
    def find_neighbors(self,click):
        i = click[0]
        j = click[1]
        neighbors = [[i - 1, j - 1], [i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1], [i + 1, j + 1], [i + 1, j - 1],
                     [i - 1, j + 1]]
        return neighbors

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []
        row = len(board)
        col = len(board[0])
        queue = [click]
        while queue:
            next_queue = []
            for clicking in queue:
                if board[clicking[0]][clicking[1]] == 'M':
                    board[clicking[0]][clicking[1]] == 'X'
                else:
                    neighbors = self.find_neighbors(clicking)
                    count = 0
                    for neighbor in neighbors:
                        if neighbor[0] in range(0, row) and neighbor[1] in range(0, col):
                            if board[neighbor[0]][neighbor[1]] == 'M':
                                count += 1

            queue = next_queue
        return


solution = Solution()
board =[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
board = [['E']]
click = [1, 2]
click = [3, 0]
print solution.updateBoard(board, click)