class Solution:
    # method 1: use hashmap to store diagnal value
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
        dict = {} # to record if diagnal element is in or not. 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dict[i-j] = matrix[i][j]
                else:
                    if dict[i-j] != matrix[i][j]:
                        return False
        return True
        