class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        memo = {}
        result = self.dfs(stickers, target, 0, memo)
        return result if result != float("inf") else -1
    
    def dfs(self, stickers, target, index, memo):
        if target == "":
            return 0

        if index == len(stickers):
            return float("inf")


        if (index, target) in memo:
            return memo[(index, target)]
        
        res = self.dfs(stickers, target, index + 1, memo)

        currSticker = stickers[index]
        nextTarget = target
        hit = False
        for char in currSticker:
            idxRemoval = nextTarget.find(char)
            if idxRemoval != -1:
                nextTarget = nextTarget[:idxRemoval] + nextTarget[idxRemoval+1:]
                hit = True
        
        if hit:
            res = min(res, self.dfs(stickers, nextTarget, index, memo) + 1)

        memo[(index, target)] = res
        return res