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


# digits = [2,0,9]
# nums2 = [0]
# test = Solution()
# print(test.second_greatest_number(digits))

# Return city name depending on their probability
# example: list[[Boston, 1] [New York, 2][Los Angeles,1]]
# if you call getCity() --> it should return New York 50% of the time not more than that
# other two 25% of the time.
# ref LC528: https://leetcode.com/problems/random-pick-with-weight/description/
    def getCity(self, cities):
        presum = [0]*len(cities)
        presum[0] = cities[0][1]
        for i in range(1, len(cities)):
            presum[i] = cities[i][1] + presum[i-1]
        total = presum[-1]
        print(presum)

        # find the first index in prefix that >= target: binary search 
        # 在prefix里搜索第一个比target大的数的(index)
        # eg [1,3], prefix区间为[0,1) [1,4) target在两个区间的比例为25%, 75%
        res = -10
        target = total*random.random()
        left, right = 0, len(presum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if presum[mid] == target:
                res = mid
            elif presum[mid] > target:
                right = mid
            else:
                left = mid
        if presum[left] >= target: #先看left, 如果left都大 说明都大
            res = left 
        else:
            res = right 
        return cities[res][0]

cities = [["Boston", 1],["New York", 3],["Los Angeles",1]]
test = Solution()
print(test.getCity(cities))
            

            