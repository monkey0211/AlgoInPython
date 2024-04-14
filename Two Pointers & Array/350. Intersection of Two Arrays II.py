

class Solution:
    # method 1: sort + two pointer
    # Time O(mlogm+nlogn) space O(1)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #followup 3? 

        if not nums1 or not nums2:
            return []
        res = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return res
    # method 2: hashmap
    # Time O(m+n)  Space: O(min(m,n)) choose smaller array to build hashmap.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter2 = collections.Counter(nums2)
        res = []
        for num in nums1:
            if num in counter2 and counter2[num] >0:
                res.append(num)
                counter2[num] -= 1
        return res
