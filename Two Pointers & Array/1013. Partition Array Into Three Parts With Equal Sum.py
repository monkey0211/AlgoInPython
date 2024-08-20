'''
1. check if the total sum of the array is divisible by three.
2. If it is, then each part should have a sum equal to one-third of the total sum.
3. iterating through the array and keeping a running sum, 
we can count how many times this target sum is achieved.
time O(n) space O(1)
'''
from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        target = sum(arr) // 3

        count = 0
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            if cur_sum == target:
                count += 1
                cur_sum = 0

            if count == 3:
                return True

        return count == 3