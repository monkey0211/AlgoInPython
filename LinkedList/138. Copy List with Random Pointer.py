"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dummy = Node(0)
        dummy.next = head

        # copy node 
        while head:
            copy = Node(head.val)
            copy.next = head.next
            head.next = copy
            head = head.next.next
        
        # copy random
        head = dummy.next
        while head and head.next: # must have head.next
            if head.random: # some random is null
                head.next.random = head.random.next #cannot reverse
            head = head.next.next #已经插入 要走两步
        
        # split
        head = dummy.next.next
        res = dummy.next.next
        while head and head.next:
            tmp = head.next.next
            head.next = tmp
            head = head.next  #已经去掉原来的head.next 只走一步
        return res
        