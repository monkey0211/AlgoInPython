# meta: digit subtraction (minus 1) given an input array
# ref: https://leetcode.com/problems/plus-one/description/ 

class Solution: 
    def minusOne(self, nums):
        if nums == [0]: return [-1]
       # i = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                while i >= 1 and nums[i] == 0:
                    nums[i] = 9
                    i -= 1
                  
                nums[i] = nums[i] -1
                return nums
            else:
                nums[i] = nums[i] -1 
                return nums


nums1 = [2,0,9]
nums2 = [0]
test = Solution()
print(test.minusOne(nums1))
print(test.minusOne(nums2))
            