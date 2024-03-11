class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 维护一个单调递增栈，逐个将元素 push 到栈里。push 进去之前先把 >= 自己的元素 pop 出来。 
        # 每次从栈中 pop 出一个数的时候，就找到了往左数比它小的第一个数（当前栈顶）和往右数比它小的第一个数（即将入栈的数）， 
        # 从而可以计算出这两个数中间的部分宽度 * 被pop出的数，就是以这个被pop出来的数为最低的那个直方向两边展开的最大矩阵面积。 
        # 因为要计算两个数中间的宽度，因此放在 stack 里的是每个数的下标。
        if not heights: return 0
        stack = [] 
        area = 0
        for i, height in enumerate(heights +[0]): #增加一个右边界
            while stack and heights[stack[-1]] > height:
                top = stack.pop()
                leftIndex = stack[-1] if stack else -1 #防止not stack: 增加一个左边界
                distance = i - leftIndex - 1
                area = max(area, distance * heights[top])
            stack.append(i)
        return area
        