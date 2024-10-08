# N inidivuals standing at various points on a road in a city. 
# Find a meeting point that the total distance traveled by all inidivuals is minimized.

# 找一个距离所有点距离(MAE定义)最小的点x -> 就是在求medium: 
# 如果奇数个数, 就是中点: nums[n//2]
# 区别正常medium(可能是小数): 如果偶数个数,是两个中间数的anywhere都可以: nums[n//2-1]-nums[n//2]
# f(x) =  min(abs_dist(x-pi))

# average O(n) time.  worst o(n^2)
class Solution:
    def findMedium(self, nums):
        index = self.quickSelect(nums, 0, len(nums) - 1, len(nums)//2)   
        return nums[index]
    
    def quickSelect(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            self.quickSelect(nums, start, right, k)
        if k >= left:
            self.quickSelect(nums, left, end, k)
        return k
        

test = Solution()
nums1 = [2,1,3,7,5,4,8,6] 
nums2 = [2,1,3,7,5,4,6]
print(test.findMedium(nums1)) 
print(test.findMedium(nums2)) 

# 1.如果二维, 可以分别对(x, y)取medium即可(因为互相独立)
# 2.如果travel cost带weights,minimize w|xi-p|的和(w>0), 可以把weights转换为频率. 
# eg. (10, 1)(15,2)(50,1) -> (10,15,15,50)再找medium 
    # each pi repeated for wi times.
# 3 if data is too large:分去不同机器

# 4. find medium in a datastream. LC295用heap
    # 左右两边两个heap: left half: maxHeap, right half: minHeap
    #如两边元素个数相等 放左边.再左边pop一个最大的换到右边. 此时左<右
    #如左=右+1, 放右边 再pop一个最小的放左边
    #最后两种情况 左==右 or 左 < 右
