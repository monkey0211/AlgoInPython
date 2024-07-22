class Solution:
    # 1.monotolic queue: 维护两个queue: 一个上升 存min, 一个下降 存max
    # 2.当max-min > limit, 移动左端点(看两个queue是否需要popleft)
    # 3.结果看区间取最大
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        left = 0
        decQueue = collections.deque() #decreasing
        incQueue = collections.deque() #increasing

        for right, num in enumerate(nums):
            while decQueue and num > decQueue[-1]: # queue里放元素的值
                decQueue.pop()
            decQueue.append(num)
            while incQueue and num < incQueue[-1]:
                incQueue.pop()
            incQueue.append(num)

            # 如果max-min > limit: 移动左端点
            while decQueue[0] - incQueue[0] > limit:
                if decQueue[0] == nums[left]:
                    decQueue.popleft()
                if incQueue[0] == nums[left]:
                    incQueue.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res



        
        