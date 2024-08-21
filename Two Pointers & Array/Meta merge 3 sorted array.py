'''
https://leetcode.com/discuss/interview-question/568482/facebook-phone-merge-3-sorted-arrays
Merge 3 sorted arrays but with no duplicate values in the final sorted array.

思路:类似merge two sorted array. 三指针 每次指向每个数组的最小值 每次选一个最小的放到ret里 
注意放入ret的时候去重 以及 每次三个指针都要check是否要移动
time O(n)  space O(1)
'''
from typing import List
def merge_sorted_arrays(arr1:List[int], arr2:List[int], arr3:List[int]) -> List[int]:
    ret = []
    if not arr1 and not arr2 and not arr3:
        return ret
    idx1, idx2, idx3 = 0, 0, 0
    while idx1 < len(arr1) or idx2 < len(arr2) or idx3 < len(arr3):
        val1 = float('inf') if idx1 >= len(arr1) else arr1[idx1]
        val2 = float('inf') if idx2 >= len(arr2) else arr2[idx2]
        val3 = float('inf') if idx3 >= len(arr3) else arr3[idx3]
        cur = min(val1, val2, val3)
        if not ret or ret[-1] != cur:
            ret.append(cur)
        if idx1 < len(arr1) and arr1[idx1] == cur:
            idx1 += 1
        if idx2 < len(arr2) and arr2[idx2] == cur:
            idx2 += 1
        if idx3 < len(arr3) and arr3[idx3] == cur:
            idx3 += 1
    return ret

# unit test
arr1 = [3,3,5,7]
arr2 = [2,3]
arr3 = [3,3]
print(merge_sorted_arrays(arr1, arr2, arr3))