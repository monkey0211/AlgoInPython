class Solution:
    # 维护一个monotonic queue放index: 单调递减. 保证头元素是最大的, 尾部每见到一个大的 就把小的pop.
    # 当头元素超出window size就popleft, 然后取window里面的头元素就是Max
    # time O(n) space O(k)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        for i in range(len(nums)):
            # 尾部如果遇到大的, 就pop
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] == i-k: # Popleft from queue because it's outside the window's leftmost (i-k)
                queue.popleft()
            if i >= k-1: #get enough k in window: append max to result
                res.append(nums[queue[0]])
        return res
            
        