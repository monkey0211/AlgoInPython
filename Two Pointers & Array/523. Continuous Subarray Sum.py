#基本题subarray sum: https://www.jiuzhang.com/solutions/subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        presum = 0
        dict = {} # store mapping : presum%k -> i
        dict[0] = -1 #这是presum代表之前的全部0~k, presum直接可以整除k 此时index假定为-1
        for i in range(len(nums)):
            presum += nums[i]
            if presum % k in dict:
                diff = i - dict[presum%k]
                if diff >= 2:
                    return True
            else:
                dict[presum%k] = i
        return False        