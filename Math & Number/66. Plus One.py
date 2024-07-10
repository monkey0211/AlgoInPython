class Solution:
    #从右往左遍历, 如果是9, reset to 0. 如果不是9, digit+1 and return.最后如果都是9, digit前面append 1
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return []
   
        # Traverse reverse
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits #直接return
        # If all digits are 9, pre-pend 1 to the list
        return [1] + digits