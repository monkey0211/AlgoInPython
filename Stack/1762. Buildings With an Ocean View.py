class Solution:
    # monotolic stack
    #从左向右 挨个把index放入stack, while stack[-1]的heights<heights[i],pop掉. 返回stack即可
    
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []

        stack =[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
        