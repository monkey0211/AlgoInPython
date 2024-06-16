class Solution:
    # binary search, 二分答案. 用mid计算getHours(mid)
    # time O(nlogm), space O(1). n:length of piles, m: max(piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left + 1 < right:
            mid = (left + right) // 2
            if self.getHours(mid, piles) <= h:
                right = mid
            else:
                left = mid
        # 先看left
        if self.getHours(left, piles) <= h:
            return left
        elif self.getHours(right, piles) <= h:
            return right

    def getHours(self, k, piles):
        hour = 0
        for pile in piles:
            hour += math.ceil(pile/k)
        return hour 

        