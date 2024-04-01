class Solution:
    # DFS: similar tp permutation
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0: return []
        res = []
        tmp = []
        board = [["." for j in range(n)] for i in range(n)]

        colSet = set()
        diagSet = set()
        vdiagSet = set()
        self.dfs(res, board, 0, colSet, diagSet, vdiagSet)
        return res

    def dfs(self, res, board, rowIndex, colSet, diagSet, vdiagSet):
        if rowIndex == len(board):
            res.append(self.createBoard(board)) #turn list format to concat string.
            return

        for j in range(len(board)):
            if j not in colSet and (rowIndex - j) not in diagSet and (rowIndex + j) not in vdiagSet:
                colSet.add(j)
                diagSet.add(rowIndex - j)
                vdiagSet.add(rowIndex + j)
                board[rowIndex][j] = "Q"

                self.dfs(res, board, rowIndex + 1, colSet, diagSet, vdiagSet)
                board[rowIndex][j] = "."

                colSet.remove(j)
                diagSet.remove(rowIndex - j)
                vdiagSet.remove(rowIndex + j)
    
    def createBoard(self, board):
        res = []
        for row in board:
            res.append("".join(row))
        return res