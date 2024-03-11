class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False
                n = i // 3*3 + j // 3
                if board[i][j] in box[n]:
                    return False
                if board[i][j] == ".": continue #need to add this. 不然也会把.加入set中
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[n].add(board[i][j])
        return True
