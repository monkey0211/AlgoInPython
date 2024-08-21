class Solution:
    # method1: Two-pointer.right pointer scanning from 1...length, 
    # 遇到和nums[right-1]不相等的就left+1, 数值放入nums[left+1]的空位
    # time O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                left += 1
                nums[left] = nums[right]
        print(nums[:left + 1]) #the array after removing duplicate
        return left + 1
    
    # method 2: binary search  time O(klogn) k个unique number
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        while right < len(nums):
            cur = nums[right]
            right = self.binary_search(nums, right, len(nums) - 1) #找等于当前值的最后一个位置 从当前位置开始二分
            if cur != nums[right]: # 如果没有duplicate, right指向的是第一个cur大的位置, 需要退后一位
                right -= 1
            nums[left] = nums[right] #用nums[left] fill the value
            right += 1
            left += 1
        print(nums[:left + 1]) #the array after removing duplicate
        return left #因为left最后又前进了一位, 所以就是长度
         

    def binary_search(self, nums: List[int], left, right) -> int:
        target = nums[left]
        while left + 1 < right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            lastPos = right
        elif nums[left] == target:
            lastPos = left
        else :
            lastPos = -1
        return lastPos