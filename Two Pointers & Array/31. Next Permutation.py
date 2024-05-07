class Solution:
    # 从右往左遍历 找到第一个peak, 拿到peak的前一个元素nums[k](此时k=i-1).
    # 再重新遍历.找peak之后的第一个比nums[k]大的元素交换nums[j], nums[peak-1]
    # (k+1)后面的元素需要重新sort 
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右往左遍历 找到第一个peak之前的元素index
        i = len(nums) - 1
        while i >= 1 and nums[i-1] >= nums[i]:
            i -= 1
        k = i - 1 #注意这里取的是nums[i-1]的index
       
        # 找到peak之后第一个比nums[k]大的元素 swap
        j = len(nums) - 1
        while j >= 1 and nums[j] <= nums[k]:
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]
        nums[k+1:] = sorted(nums[k+1:])
    
        