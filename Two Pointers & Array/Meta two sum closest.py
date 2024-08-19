'''
Given an int array nums and an int target. 
Find two integers in nums such that the sum is closest to target.

Example 1:
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: [4, 5]

Example 2:
Input: nums= [-1, 2, 1, -4], target = 4
Output: [2, 1]

Time complexity: O(nlogn).
Space complexity: O(1).
'''
from typing import List

def two_sum_closest(nums:List[int], target:int) -> List[int]:
    if not nums or len(nums) < 2:
        return []
    
    nums.sort()
    ret = [-1] * 2
    min_diff = float("inf")
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        diff = abs(target - sum)
        if diff < min_diff:
            min_diff = diff
            ret[0], ret[1] = nums[left], nums[right]
        if sum < target: # 移动left 使得sum下一次更大一些 更靠近target
            left  += 1
        elif sum > target: # 移动right 使得sum下一次更小一些 更靠近target
            right -= 1
        else:             # sum==target 不会有更接近的答案了 直接break
            break
    return ret


# unit test
nums1 = [1, 2, 3, 4, 5]
target1 = 10
print(two_sum_closest(nums1, target1))
nums2 = [-1, 2, 1, -4]
target2 = 4
print(two_sum_closest(nums2, target2))
