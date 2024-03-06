class Solution:
 
# 1. two pointer:  time o(n) space o(1)
# while left <= right, 哪边小移动哪边 并更新maxLeft or maxRight
# if maxleft < maxright（左边装水): 比较current height[i] and maxleft. 如果current小，可以装水water+=difference. if larger, 水会流走(leftmax更新之后差为零)
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, rightBound in enumerate(height):
            while stack and height[stack[-1]] < rightBound:
                top = stack.pop()
                if stack:
                    distance = i - stack[-1] - 1
                    minBound = min(rightBound, height[stack[-1]])
                    res += distance * (minBound - height[top])
            stack.append(i)
        
        return res
    
#2. stack: 单调栈 递减. 每遇到一个可以递增的点, 计算积水宽*长, 累加.
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, rightBound in enumerate(height):
            while stack and height[stack[-1]] < rightBound:
                top = stack.pop()
                if stack:
                    distance = i - stack[-1] - 1
                    minBound = min(rightBound, height[stack[-1]])
                    res += distance * (minBound - height[top])
            stack.append(i)
        
        return res