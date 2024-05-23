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
    
    # method 2: compare with previous diagnal element
    # space o(1) compare: matrix[i][j] != matrix[i-1][j-1]

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
     
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True
        