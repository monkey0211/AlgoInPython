class TwoSum:
    # 只能用hashmap. 
    def __init__(self):
        self.nums = []
        
    def add(self, number: int) -> None:
        self.nums.append(number)
        
    def find(self, value: int) -> bool:
        dict = set() # must be local variable
        for i in range(len(self.nums)):
            if value - self.nums[i] not in dict:
                dict.add(self.nums[i])
            else:
                return True   
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)