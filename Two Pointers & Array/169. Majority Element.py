
# Explanation:
# The algorithm starts by assuming the first element as the majority candidate and sets the count to 1.
# As it iterates through the array, it compares each element with the candidate:
# a. If the current element matches the candidate, it suggests that it reinforces the majority element because it appears again. Therefore, the count is incremented by 1.
# b. If the current element is different from the candidate, it suggests that there might be an equal number of occurrences of the majority element and other elements. Therefore, the count is decremented by 1.
# Note that decrementing the count doesn't change the fact that the majority element occurs more than n/2 times.
# If the count becomes 0, it means that the current candidate is no longer a potential majority element. In this case, a new candidate is chosen from the remaining elements.
# The algorithm continues this process until it has traversed the entire array.
# The final value of the candidate variable will hold the majority element.
# Exp
# lanation of Correctness:
# The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array. This assumption guarantees that even if the count is reset to 0 by other elements, the majority element will eventually regain the lead.

# Let's consider two cases:

# If the majority element has more than n/2 occurrences:
# The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

# If the majority element has exactly n/2 occurrences:
# In this case, there will be an equal number of occurrences for the majority element and the remaining elements combined.
# However, the majority element will still be selected as the final candidate because it will always have a lead over any other element.
# In both cases, the algorithm will correctly identify the majority element.

# The time complexity of the Moore's Voting Algorithm is O(n) since it traverses the array once.

class Solution:
    # Aaron submission
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

        