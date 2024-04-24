class SparseVector:
    #先把一个vector(可以选数量更sparse的list)的index放入dict, 等另一个逐个对比
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dict[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i in vec.dict: #如何看到vec.dict?
            if i in self.dict:
                total += self.dict[i] * vec.dict[i]
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)