# meta: digit subtraction (minus 1) given an input array
# ref: https://leetcode.com/problems/plus-one/description/ 

class Solution: 
    def minusOne(self, nums):
        if nums == [0]: return [-1]
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                while i >= 1 and nums[i] == 0:
                    nums[i] = 9
                    i -= 1
                  
                nums[i] = nums[i] -1
                res = nums
                break
            else:
                nums[i] = nums[i] -1 
                res = nums
                break
        
        #去掉leading zero
        j = 0
        while j <= len(nums) - 1 and nums[j] == 0:
            j += 1
        res = nums[j:]
        return res

nums1 = [2,0,9]
nums2 = [1,0]
test = Solution()
print(test.minusOne(nums1))
print(test.minusOne(nums2))
            