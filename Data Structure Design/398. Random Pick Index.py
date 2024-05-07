class Solution:
    # hashmap: 存value-> [index List]
    # random函数: rand.choice(list) 随机从list里取一个数, 概率相同.
    def __init__(self, nums: List[int]):
        self.dict = collections.defaultdict(list)
        for i in range(len(nums)):
            self.dict[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        indexList = self.dict[target]
        return random.choice(indexList)
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)