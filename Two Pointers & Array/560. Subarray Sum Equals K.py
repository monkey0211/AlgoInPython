#基本题subarray sum: https://www.jiuzhang.com/solutions/subarray-sum/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefix = 0
        cnt = 0
        counter = {} # 存之前的prefix
        counter[0] = 1 
        for i in range(len(nums)):
            prefix += nums[i]
       
            if (prefix - k) in counter:
                cnt += counter[prefix-k]
            if prefix not in counter:
                counter[prefix] = 1
            else:
                counter[prefix] += 1             
        return cnt 
