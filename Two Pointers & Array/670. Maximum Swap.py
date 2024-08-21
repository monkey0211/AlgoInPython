class Solution:
    # time O(n) space O(1)
    # 站在nums[i]: 寻找i右边的maxValue, 交换. 注意如果有两个相同的maxValue, 需要交换的是最后面的那一个 
    def maximumSwap(self, num: int) -> int:
        if num < 10: return num

        nums = list(str(num))
    
        for i in range(len(nums) - 1):
            #1.from left to right: search the first increasing point, call it max
            if nums[i] < nums[i+1]:
                pivot = i + 1
            
                #2.from max to remaining, search for next farest max
                for j in range(i+1, len(nums)):
                    if nums[j]>= nums[pivot]:
                        pivot = j
                #3. from beginning, search for first item smaller than pivot.
                for k in range(i+1):
                    if nums[k] < nums[pivot]:
                        nums[k], nums[pivot] = nums[pivot], nums[k]
                        return int("".join(nums))
        return num

            

