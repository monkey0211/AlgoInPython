class Solution:
    # monotolic stack
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []

        stack =[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
        