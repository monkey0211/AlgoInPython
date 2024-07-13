
class Solution: 
    def substractTwoIntegers(self, nums1, nums2):
        i, j = len(nums1) - 1, len(nums2) - 1
        res = []
        borrow = 0
        digit = 0

        while i >= 0 or j >= 0:
            a = nums1[i] if i >= 0 else 0
            b = nums2[j] if j >= 0 else 0
            digit = a - b + borrow
            print(digit)
            if digit < 0:
                borrow = -1
                res.append(digit + 10)
            else:
                borrow = 0
                res.append(digit)
            i -= 1
            j -= 1
        #最后如果有剩余borrow=-1, 说明nums1<nums2,可以switch两个array再做
        # if borrow == -1:
        #     return total*(-1)
        #需要reverse, 然后去掉leading zero
        print(res)
        res = reversed(res) 
        k = 0
        while k < len(res) and res[k] == 0:
            k += 1
        return res[k:]
    
    
nums1 = [3, 4, 5]
nums2 = [2, 2, 1] 
test = Solution()
print(test.substractTwoIntegers(nums1, nums2))
        
        
                
            
            
            
        