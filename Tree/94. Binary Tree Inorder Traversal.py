from typing import List
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # method 1: traverse
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
               
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
        
    # method 2: interative. stack
    # 先找到deep left node, until left tree is all done.  
    # find first right node, repeat finding deep left node.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res = []
        stack = []
        #1.确定起点: leftmost node
        while root:
            stack.append(root)
            root = root.left
        
        #2.pop element from stack and append to res. then check right node.
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
        return res

'''
变种问法:
Given a Binary Tree and an input array. The task is to create an Iterator that utilizes next() and hasNext() functions 
to perform Inorder traversal on the binary tree.
思路与上面的method2一样 套一个iterator的壳
''' 
class InorderIterator:
    def __init__(self, root:TreeNode):
        self.traversal = []
        self.moveLeft(root)
 
    def moveLeft(self, current:TreeNode):
        while current != None:
            self.traversal.append(current)
            current = current.left
 
    def hasNext(self):
        return len(self.traversal) > 0
 
    def next(self):
        if not self.hasNext():
            raise Exception('No such element Exists')
        current = self.traversal.pop()
        if current.right != None:
            self.moveLeft(current.right)
        return current

'''
# unit test 先创建树 再初始化iter
root = Node(8)
root.right = Node(9)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.right.right = Node(5)
 
itr = InorderIterator(root)
try:
    print(itr.next().data)
    print(itr.hasNext())
    print(itr.next().data)
    print(itr.next().data)
    print(itr.next().data)
    print(itr.hasNext())
    print(itr.next().data)
    print(itr.next().data)
    print(itr.hasNext())
except Exception as e:
    print("No such element Exists")
'''