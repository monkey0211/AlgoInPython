class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dict = collections.defaultdict(list)
        res = []
        for i in range(len(nums)):
            for j in range(len(nums[i])): #注意是nums[i]
                dict[i+j].append(nums[i][j])
        for k in dict.values():
            res.extend(k[::-1])
        return res

        