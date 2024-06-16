from typing import List
class Solution:
    # 遍历数组, 凡事遇到startIndex就+value, 到endIndex后一位的时候-value->get all the changes for each element.
    # 最后计算prefix sum. we don't want to add incrementValue until end.
    # time O(n+k), space O(1)
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length
        for start, end, val in updates:
            res[start] += val
            end += 1
            if end < len(res):
                res[end] -= val
        
        # step 2. get the prefix sum of res array.
        for i in range(1, len(res)):
            res[i] += res[i-1]
        return res

    # Doordash: 改为2D matrix, updates是每个row的updates. 
    def get2DModifiedArray(self, matrix, updates: List[List[int]]) -> List[int]:
        changes = [0]*len(matrix)
        for start, end, val in updates:
            changes[start] += val
            end += 1
            if end < len(changes):
                changes[end] -= val
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    matrix[i][j] = changes[i]
                else:
                    matrix[i][j] = matrix[i-1][j] + changes[i]
        return matrix

matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
updates = [[1,3,2],[2,4,3],[0,2,-2]]
test = Solution()
print(test.get2DModifiedArray(matrix, updates))
        
            