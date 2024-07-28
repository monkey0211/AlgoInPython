# return the smallest character that is strictly larger than the search character,
# otherwise return the first character in the String.

# method1: 先按照mean分leftHalf[] and rightHalf[], 然后merge two sorted list. 注意leftHalf是reversed(降序)
# 如果a<0: rightHalf reverse即可.

# method2: 先用二分找到最低点的index O(logN), 然后按照这个点分别看left and right O(n) -> o(logN + N)
# 如果large dataset cannot fit into one machine. 用上面这个方法
class Solution:
    def computeSortedFx(inputArray, a, b, c):
        if a <= 0:
            return None
        
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
        return res

test = Solution()
nums = []
print(test.computeSortedFx(nums))
        
        