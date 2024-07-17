import random


class Solution: 
    def second_greatest_number(self, digits):
        # Sort digits in descending order to get the greatest number
        digits.sort(reverse=True)
        
        # Find the first position from the right where the digit is smaller than the previous digit
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                # Find the largest digit to the right of digits[i-1] that is smaller than digits[i-1]
                max_digit_index = i
                for j in range(i, len(digits)):
                    if digits[j] < digits[i - 1] and digits[j] > digits[max_digit_index]:
                        max_digit_index = j
                # Swap the digits
                digits[i - 1], digits[max_digit_index] = digits[max_digit_index], digits[i - 1]
                # Sort the digits to the right of i-1 in descending order
                digits = digits[:i] + sorted(digits[i:], reverse=True)
                break
        else:
            # If no such digit is found, it means all digits are in descending order
            return None
    
        # Convert the list of digits back to an integer
        return int(''.join(map(str, digits)))


digits = [2,0,9]
nums2 = [0]
test = Solution()
print(test.second_greatest_number(digits))

