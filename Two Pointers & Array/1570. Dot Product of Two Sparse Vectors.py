class SparseVector:
    # method 1: build a set to store the index of non-zero element
    # check if new vec.nums[i]!=0 and in self.set, calculate total.
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.set = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.set.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if not vec: return 0
        total = 0
        for i in range(len(vec.nums)):
            if i in self.set and vec.nums[i] != 0:
                total += self.nums[i] * vec.nums[i]
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

    # method 2: create self.pairs = <index, value> for non-zeros. 
    # two pointers to iterate through the two vectors to calculate the dot product.
    def __init__(self, nums: List[int]):
       self.pairs = [] #build (index, value) pair
       for i in range(len(nums)):
        if nums[i] != 0:
            self.pairs.append((i, nums[i]))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if not vec: return 0
        total = 0
        p, q = 0, 0
        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                total += self.pairs[p][1]*vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        return total