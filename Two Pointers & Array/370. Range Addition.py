class Solution:
    # 遍历数组, 凡事遇到startIndex就+value, 到endIndex后一位的时候-value
    # 最后计算prefix sum. we don't want to add incrementValue until end. 
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

        