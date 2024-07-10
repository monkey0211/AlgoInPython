class Solution:
    # two pointer + sliding window. l,r风别是最后结果的左右端点
    # 1.先用right遍历 遇到0就把k-1. 就是先用掉所有的k, 找到一个当前window
    # 2.更新window: 每次当k<0, 看left, 如果左端点是0, k恢复0.然后left+1
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: #cnt目前找到了几个0(可以作为1)
                k -= 1
            #找到了一个window 需要更新window
            if k < 0: 
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

        