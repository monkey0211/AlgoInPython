class Solution:
    # binary search.time  O(nlogn) space O(n)
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        # create tuple of (dificilty, profit) and sort by difficulty
        diff_prof = [[difficulty[i], profit[i]]for i in range(len(profit))]
        diff_prof.sort(key = lambda x: (x[0], x[1]))

        # the maximum profit at each difficulty. eg [1,99][2,1]->[1,99][2,99]
        prev = diff_prof[0][1]
        for i in range(len(diff_prof)):
            diff_prof[i][1] = max(diff_prof[i][1], prev)
            prev = diff_prof[i][1]

        maxProfit = 0
        for target in worker:
            # binary search to search for the max number that's smaller(or equal) than target
            index = self.binarySearch(target, diff_prof)
            if target >= diff_prof[index][0]: # 防止有out of index
                maxProfit += diff_prof[index][1]
        return maxProfit

    def binarySearch(self, target, diff_prof):
        left, right = 0, len(diff_prof) - 1
        while left +1 < right:
            mid = (left + right) // 2
            if diff_prof[mid][0] == target:
                left = mid
            elif target < diff_prof[mid][0]:
                right = mid
            else:
                left = mid
        if diff_prof[right][0] <= target:
            return right
        else:
            return left



        