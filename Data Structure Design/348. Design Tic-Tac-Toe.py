class TicTacToe:

    def __init__(self, n: int):
        #直接定义row/col array as sum of the row/col
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.vdiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        #不能直接用player 计算结果player*n, 需要assign新的值分别看3/-3. eg if sum(row) == 3 可能是(1,2,0) not (1,1,1)
        #定义player1: 1 player2: -1
        if player == 1:
            val = 1
        else:
            val = -1
        self.row[row] += val
        self.col[col] += val
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n:
            return player
        if row == col:
            self.diag += val
            if abs(self.diag) == self.n:
                return player
        if row + col == self.n - 1:
            self.vdiag += val
            if abs(self.vdiag) == self.n:
                return player
        return 0
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)