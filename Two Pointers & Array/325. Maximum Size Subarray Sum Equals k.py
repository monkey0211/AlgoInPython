class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefix = 0
        maxLen = 0
        dict = {} #dict[prefix] = index
        dict[0] = -1

        for i in range(len(nums)):
            prefix += nums[i]
           
            if (prefix - k) in dict:
                length = i - dict[prefix-k]
                maxLen = max(maxLen, length)
            if prefix not in dict: # 不论prefix-k如何, 先看自己, 放入 dict. 不是prefix-k not in dict. 
                dict[prefix] = i
        return maxLen