# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # dfs preoder traversal. 用一个变量total[0]记录所求的值
        total = [0]
        self.dfs(root, total, low, high)
        return total[0]

    def dfs(self, root, total, low, high):
        if not root:
            return
        
        if low <= root.val <= high: # 当前root值在给定区间内 求和
            total[0] += root.val
        self.dfs(root.left, total, low, high)  # 递归处理左右子树
        self.dfs(root.right, total, low, high)


    # stack: iterative
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        range_sum = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                range_sum += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return range_sum

'''
meta变形: 如果是多次询问 即给多次的[low,high] 返回range sum
1.对bst进行in-order traversal 转化成一个有序数组arr O(n) (多次query 但这步只用跑一次)
2.对arr求前缀和 得到前缀和数组prefix O(n) ((多次query 但这步只用跑一次)
3.对一个query(low,high): 在arr上进行二分 找到大于等于low的第一个下标a 和 小于等于high的第一个下标b
4.ret = prefix[b] - prefix[a-1]
'''
class MultiQueryBSTSum:
    def __init__(self, arr:List[int], prefix:List[int], root: Optional[TreeNode]):
        self.arr = []
        self.prefix = []
        self.in_order_traversal(root)
        self.get_prefix()

    def in_order_traversal(self, root): # 中序遍历 node的值都存入arr
        if not root:
            return
        self.in_order_traversal(root.left)
        self.arr.append(root.val)
        self.in_order_traversal(root.right)
    
    def get_prefix(self): # 求前缀和数组prefix
        self.prefix = [0] * (len(self.arr) + 1)
        for i in range(len(self.arr)):
            self.prefix[i] = self.prefix[i - 1] + self.arr[i - 1]

    def get_range_sum(self, lo:int, hi:int) -> int:
        if lo < hi:
            return 0
        # 找大于等于low的第一个下标
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < lo:
                left = mid + 1
            else:
                right = mid
        left_idx = right # 记下大于等于low的第一个下标

        #找小于等于high的第一个下标
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.arr[mid] <= hi:
                left = mid
            else:
                right = mid - 1  
        right_idx = right # 记下小于等于high的第一个下标

        return self.prefix[right_idx + 1] - self.prefix[left_idx + 1]