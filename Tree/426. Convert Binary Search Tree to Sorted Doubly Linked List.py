"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    # DFS function: get head and tail. 分四种情况讨论(none left non right, not node.left, not node.right etc)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        if root is None:
            return None
        head, _ = self.getHeadAndTail(root)
        return head
        
    def getHeadAndTail(self, root: "Node") -> tuple["Node", "Node"]:
        # The base case: if we are at a leaf node, we return a doubly linked
        if not root.left and not root.right:       
            root.left = root
            root.right = root
            return root, root

        if root.left is None:
            # Only the right side is non-null: 
            right, tail = self.getHeadAndTail(root.right)
            
            # The current root becomes the new head of linked list
            root.right = right
            right.left = root
            
            # The tail must be circularly linked back to the new head
            root.left = tail
            tail.right = root
            
            return root, tail

        elif root.right is None:

            head, left = self.getHeadAndTail(root.left)
            
            # The current root becomes the new tail of the linked list
            root.left = left
            left.right = root
            
            # The head must be circularly linked back to the new tail
            head.left = root
            root.right = head
            
            return head, root
        else:
            left_head, left_tail = self.getHeadAndTail(root.left)
            right_head, right_tail = self.getHeadAndTail(root.right)
            
            # The root must be linked in between the tail of the left list and the
            # head of right list
            root.left = left_tail
            left_tail.right = root

            root.right = right_head
            right_head.left = root
            
            # The head of the left list and tail of the right list must then be
            # circularly linked to each other
            left_head.left = right_tail
            right_tail.right = left_head
            
            return left_head, right_tail
    
    # method 2: stack
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        stack = []
        res = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            res.append(node)
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
        
        #connect nodes within res:
        for i in range(len(res)-1):
    
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]

