
class Solution:
    # 找到此数组的next greater permutation number.
    # 从右往左遍历 找到第一个peak, 拿到peak的前一个元素nums[k](此时k=i-1).
    # 再重新遍历.找peak之后的最后一个比nums[k]大的元素 交换nums[j], nums[peak-1]
    # (k+1)后面的元素需要重新sort 
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # 从右往左遍历 找到第一个peak之前的元素index
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums.reverse()
            return 
        pivot = i # peak element
        k = i - 1 #注意这里取的是nums[i-1]的index
        
       
        # 找到peak之后最后一个比nums[k]大的元素 swap
        j = pivot
        while j <= len(nums) - 1 and nums[j] > nums[k]:
            j += 1

        nums[k], nums[j-1] = nums[j-1], nums[k]
        nums[k+1:] = reversed(nums[k+1:])
    
        