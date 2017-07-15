"""
author: fangren
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0:
            return 0
        if len(board[0]) == 1:
            if ['X'] in board:
                return 1
            else:
                return 0
        row = len(board)
        col = len(board[0])
        memory = []
        ships = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    if (i,j) not in memory:
                        ships += 1
                        memory.append((i,j))
                        i_new = i+1
                        j_new = j+1
                        while i_new < row:
                            if board[i_new][j] == 'X':
                                memory.append((i_new, j))
                            else:
                                break
                            i_new = i_new + 1
                        while j_new < col:
                            if board[i][j_new] == 'X':
                                memory.append((i, j_new))
                            else:
                                break
                            j_new += 1
        return ships




solution = Solution()
# board = [['.', '.', 'X', 'X']]
# board = [['.'],['.'],['X'],['X']]
#board = [['.', '.', 'X', 'X'],['.', '.', '.', '.'],['.', '.', 'X', 'X']]
# board = ["X..X","...X","...X"]

board = ["X.X"]
board = ['']
board = ['.']
board = ['','']
print solution.countBattleships(board)