# return the smallest character that is strictly larger than the search character,
# otherwise return the first character in the String.

# method3(不好): 先用二分找到最低点的index O(logN), 然后按照这个点分别看left and right O(n) -> o(logN + N)
# 如果large dataset cannot fit into one machine. 用上面这个方法

class Solution:
    # method1(下面): 先按照mean分leftHalf[] and rightHalf[], 然后merge two sorted list. 注意leftHalf是reversed(降序)
    # 如果a<0: rightHalf reverse即可.
    def computeSortedFx(inputArray, a, b, c):
        
        mean = -b/(2*a)
        left = []
        right = []
        for i in range(len(inputArray)):
            value = a * inputArray[i] * inputArray[i] + b * inputArray[i] + c
            if inputArray[i] <= mean:
                left.append(value)
            else:
                right.append(value)
        
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
        
        return res if a > 0 else res.reverse()

# test = Solution()
# nums = []
# print(test.computeSortedFx(nums))

#method 2: 直接双指针比较, if a > 0,开口朝上, 此时l, r 都是相对大的, 先选最大的放. res list从后向前. 
# if a<0, 先放小的, res从左到右
# https://leetcode.com/problems/sort-transformed-array/
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
            n = len(nums)
            index = 0 if a < 0 else n-1
            l, r, ans = 0, n-1, [0] * n
            while l <= r:
                l_val, r_val = self.quadratic(nums[l],a, b, c), self.quadratic(nums[r],a, b, c)
                if a >= 0: #开口朝上, 此时l, r 都是相对大的, 先选最大的放. index-1从后向前
                    if l_val > r_val:
                        ans[index] = l_val 
                        l += 1
                    else:    
                        ans[index] = r_val 
                        r -= 1
                    index -= 1
                else: #开口朝下, 此时先选最小的放. index+1从左向右
                    if l_val > r_val:
                        ans[index] = r_val 
                        r -= 1
                    else:    
                        ans[index] = l_val 
                        l += 1
                    index += 1
            return ans

    def quadratic(self, x, a, b, c):
        return a*x*x + b*x + c 
            
            
            