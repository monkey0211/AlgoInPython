'''
Given a binary array nums, 
return the maximum length of a contiguous subarray with an equal number of 0 and 1.
思路: 前缀和
prefix[i]: 前i个数中 1的个数减去0的个数
区间示意图:
<----->   <---->
0    j-1  j    i 
[i,i]中   1的个数减去0的个数: prefix[i] - prefix[i-1]
[i-1,i]中 1的个数减去0的个数: prefix[i] - prefix[i-2]
...
[j,i]中   1的个数减去0的个数: prefix[i] - prefix[j-1]

用diff_to_idx这个dict 记录第一次出现x个“1-0”差值时 对应数组中的位置i

时间O(n) 空间O(n)
'''
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        diff_to_idx = {}   # 记录1的个数减去0的个数为key时 对应第i个数组元素 
        diff_to_idx[0] = 0 # 注意要初始化 意义是第0个数(还没数字)时 “1-0”的个数为0
        zero_num, one_num = 0, 0
        ret = 0
        for i in range(1, n + 1):
            cur = nums[i - 1]
            if cur == 0:
                zero_num += 1
            else:
                one_num += 1
            num_diff = one_num - zero_num
            
            # 之前出现过diff 距离肯定比当前的距离长 所以不更新diff_to_idx
            if num_diff in diff_to_idx:
                ret = max(ret, i - diff_to_idx[num_diff])
            else:  # 第一次出现该diff 更新map
                diff_to_idx[num_diff] = i
        return ret