
from typing import List


class Solution:
    # in-place modify. need to go backward.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
    
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    
    # meta version: output no duplicates 
    def merge1(self, nums1: List[int], nums2: List[int]) -> None:
       
        res = []
        i, j= 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if not res:
                    res.append(nums1[i])
                elif res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
            else:
                if not res:
                    res.append(nums2[j])
                elif res[-1]!= nums2[j]:
                    res.append(nums2[j])
                j += 1
        
    
        while i < len(nums1):
            if res and res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
     
        while j < len(nums2):
            if res and res[-1]!= nums2[j]:
                res.append(nums2[j])
            j += 1
        return res

test = Solution()
print(test.merge1([1,2,3],[2,4,6]))