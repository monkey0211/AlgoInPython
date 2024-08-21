'''
思路: 二分 + 双指针
1. 先二分出 离x最近的一个位置. 这里可以二分大于等于x的第一个元素
2. 然后从该元素的位置往左右两边扩展 i,j指针分别往左右走 看谁离x更近 每次更近的指针往远处扩展
3. 直到[i,j]之间有k个元素
时间O(logn + k) 空间O(1)
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or k <= 0:
            return []
        
        # binary search to find the first element >= x
        left = 0
        right = len(arr) - 1
        while left < right: # when loop exits, left == right
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid # here it must be mid
            else:
                left = mid + 1 # here it must be mid + 1
        
        # linear seach k elements
        # 二分得到的位置 是大于等于x的 最小的位置
        # 但是答案可能选择k个数都小于x
        # 所以这里要判断 是选择大于等于x的最小值好 还是小于等于x的最大值好
        # 即: right-1 和 right 哪个离x更近
        if right and abs(x - arr[right - 1] <= abs(arr[right] - x)):
            right -= 1
        
        i = right
        j = right
        # 当前区间里已经有一个数了 所以走k-1次即可
        for u in range(k-1):
            if i == 0: # i走到头了 只能让j走
                j += 1
            elif j == len(arr) - 1: # j走到头了 只能让i走
                i -= 1
            else: # 比较i,j哪个元素更近
                if abs(arr[i-1] - x) <= abs(arr[j+1] - x):
                    i -= 1
                else:
                    j += 1
        ret = []
        for u in range(i, j+1): # 收集答案
            ret.append(arr[u])
        return ret
