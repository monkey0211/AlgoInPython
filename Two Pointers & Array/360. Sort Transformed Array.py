class Solution:
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
        