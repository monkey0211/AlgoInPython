class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        res = []
        dict = {}

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dict[stack[-1]] = nums2[i] # hashmap has key: element->next greater element
                stack.pop()
                
            stack.append(nums2[i])
        
        for element in stack: #if cannot find the next greater element, assign -1
            dict[element] = -1
        for i in range(len(nums1)):
            res.append(dict[nums1[i]])
        return res