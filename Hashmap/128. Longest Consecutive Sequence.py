class Solution:
    # method 1: dict. time O(n), space o(n)
    # 1.nums放入set. 
    # 2.for每一个元素, 当number-1 not in dict, find the lower bound. when number+1 not in dict, find the upper bound
    # 3.用完加入seen, 不需要再看
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)
        seen = set()
        maxcnt = 0
        for num in nums:
            
            if num not in seen:
                seen.add(num)
                cnt = 1
                low = num - 1
                while low in numset:
                    seen.add(low)
                    cnt += 1
                    low -= 1
                high = num + 1
                while  high in numset:
                    seen.add(high)
                    cnt += 1
                    high += 1              
                maxcnt = max(maxcnt, cnt)
        return maxcnt
        
# method 2: reduce space
# 1.nums放入set. 
# 2.for每一个元素, 当number-1 not in dict, find the lower bound. when number+1 not in dict, find the upper bound 用完把自己从set删除(减小复杂度). 
# 3. 求max(hi-lo-1, maxlen)