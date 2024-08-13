class Solution:
# binary search Time O(log(min(m, n)) space O(1)
# 对小的数组进行二分 则另一个切分的长度为(m+n+1)//2 - par1
# 需要保证左边的最大都比右边的最小**小**
# nums1: [1,3 | 5,7]
#         0 1   2 3
# nums2: [3,6,11 | 15,18]
#        0  1  2    3   4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return nums2[len(nums2)//2] if len(nums2)%2 != 0 else (nums2[len(nums2)//2 - 1] + nums2[len(nums2)//2])/2

        if not nums2:
            return nums1[len(nums1)//2] if len(nums1)%2 != 0 else (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        #left, right 指的是partition位置(分割的左边有多少个数) 所以要取的是长度 不能len-1
        left1, right1 = 0, len(nums1)
        while left1 <= right1:
            mid1 = (left1+right1)//2
            mid2 = (len(nums1) + len(nums2) +1)//2 - mid1 #nums2的左边还需要多少个

        #如果其中一边切分之后为空  设置默认值为最小/最大
            maxleft1 = - float("inf") if mid1 == 0 else nums1[mid1-1]
            minright1 = float("inf") if mid1 == len(nums1) else nums1[mid1]
            maxleft2 = - float("inf") if mid2 == 0 else nums2[mid2-1]
            minright2 = float("inf") if mid2 == len(nums2) else nums2[mid2]
            #判断条件 分奇偶
            if maxleft1 <= minright2 and maxleft2 <= minright1: #找到了
                if (len(nums1) + len(nums2)) %2 == 0:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) /2
                else:
                    return max(maxleft1, maxleft2)
            #左边太大(取多了) 扔掉右边; 左边太小(取少了) 扔掉左边
            elif maxleft1 > minright2:
                right1 = mid1 - 1
            else:
                left1 = mid1 + 1