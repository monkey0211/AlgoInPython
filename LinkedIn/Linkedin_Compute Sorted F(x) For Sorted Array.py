# return the smallest character that is strictly larger than the search character,
# otherwise return the first character in the String.

# method3(不好): 先用二分找到最低点的index O(logN), 然后按照这个点分别看left and right O(n) -> o(logN + N)
# 如果large dataset cannot fit into one machine. 用上面这个二分方法先找到最低index 对应找出机器的index

class Solution:
    # method1(下面): 先按照mean分leftHalf[] and rightHalf[], 然后merge two sorted list. 注意leftHalf是reversed(降序)
    # 如果a<0: rightHalf reverse即可.
    # time o(n), space o(n)
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            ans = [b * nums[i] + c for i in range(len(nums))]
            if b > 0:
                return ans
            elif b < 0:
                return reversed(ans)
            else:
                return [c] * len(nums)

        mean = -b/(2*a)
        left = []
        right = []
        for i in range(len(nums)):
            value = a * nums[i] * nums[i] + b * nums[i] + c
            if nums[i] <= mean:
                left.append(value)
            else:
                right.append(value)
        if a < 0: 
            right.reverse()
            left.reverse()
       
        res = []
        i = len(left) - 1
        j = 0
        while i >= 0 and j <= len(right) - 1:
            if left[i] <= right[j]:
                res.append(left[i])
                i -= 1
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
        while i >= 0:
            res.append(left[i])
            i -= 1
        while j <= len(right) - 1:
            res.append(right[j])
            j += 1
        
        return res 

#method 2: 直接双指针比较, if a > 0,开口朝上, 此时l, r 都是相对大的, 先选最大的放. res list从后向前. 
# if a<0, 先放小的, res从左到右
# https://leetcode.com/problems/sort-transformed-array/
# time o(n) space o(1)

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
            index = 0 if a < 0 else len(nums) - 1
            l, r = 0, len(nums) - 1
            res = [0]*len(nums)
            while l <= r:
                l_val, r_val = self.quadratic(nums[l],a, b, c), self.quadratic(nums[r],a, b, c)
                if a >= 0: #开口朝上, 此时l, r 都是相对大的, 先选最大的放. index-1从后向前
                    if l_val > r_val:
                        res[index] = l_val 
                        l += 1
                    else:    
                        res[index] = r_val 
                        r -= 1
                    index -= 1
                else: #开口朝下, 此时先选最小的放. index+1从左向右
                    if l_val > r_val:
                        res[index] = r_val 
                        r -= 1
                    else:    
                        res[index] = l_val 
                        l += 1
                    index += 1
            return res

    def quadratic(self, x, a, b, c):
        return a*x*x + b*x + c 
            
            
            