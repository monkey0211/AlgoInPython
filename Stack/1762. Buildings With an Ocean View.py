class Solution:
    # monotolic stack
    #从左向右 挨个把index放入stack, while stack[-1]的heights<heights[i],pop掉. 返回stack即可
    
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []

        stack =[] # 栈中元素是下标 对应的高是单调减的
        for i in range(len(heights)):
            # 占顶元素对应的高 小于等于当前元素的高 pop栈顶  
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack