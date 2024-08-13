class Solution:
    # dfs要return T/F 代表是否可以找到这样的number
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        box = [set([]) for i in range(9)]
        cnt = 81
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    cnt -= 1  #用cnt计数 for every value found, cnt-1
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3)*3 + j//3].add(board[i][j])
        self.dfs(board, row, col, box, cnt)

    def dfs(self, board, row, col, box, cnt) -> bool:
        #解决 if possible to fill board[i][j] with number = 'num'问题
        if cnt == 0:
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    continue  #必须有
                for num in ["1","2","3","4","5","6","7","8","9"]:
                    if num not in row[i] and num not in col[j] and num not in box[(i//3)*3 + j//3]:
                        row[i].add(num)
                        col[j].add(num)
                        box[(i//3)*3 + j//3].add(num)
                        board[i][j] = num

                        if self.dfs(board, row, col, box, cnt - 1):
                            return True  #找到就return跳出
                        row[i].remove(num)
                        col[j].remove(num)
                        box[(i//3)*3 + j//3].remove(num)
                        board[i][j] = "." #变回去
                return False  # False和for对齐 代表前面的True都不符合

