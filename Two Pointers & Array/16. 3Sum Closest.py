'''
leetcode原题是返回sum of the three integers.
思路: sort + two pointers
这道题只是要求返回最近的和 所以没有考虑去重等因素. 如果要返回三个数本身 需要考虑去重
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf") # 初始化一个diff 表示三数之和与target的diff
        nums.sort()         # sort原数组
        for i in range(len(nums)): # 遍历三数之中的一个数 然后双指针另外两个
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff): # 找到一个更好的diff
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0: # 找到恰好三数之和等于target 不会有更好的diff了 直接break即可
                break
        return target - diff