"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # 三种情况: 
    # 1. no head
    # 2. insertVal >= max or inserVal <= min: 插入max->insertVal->min
    # 3. 都不是 就直接插入
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        # https://www.youtube.com/watch?v=xhtmKGsLnPM
        # case 1: if not head 直接形成self-circle
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode

        dummy = Node(-1)
        dummy.next = head

        #先找到原linkedList的最大node和最小node
        while head.next != dummy.next and head.val <= head.next.val: # 需要除去self-circle的情况case1. eg head = [1], insertVal=0
            head = head.next
        minNode = head.next

        # case 2: if insertVal>max or <min直接插入该位置 连接
        if head.val <= insertVal or insertVal <= minNode.val:
            newNode.next = minNode
            head.next = newNode
        else:
            # case 3: 正常插入. compare head.next < insertVal
            while head.next.val < insertVal: #此时需要让head.next<insert, 否则head->insert->head.next不可以
                head = head.next
 
            nextNode = head.next
            newNode.next = nextNode
            head.next = newNode
        return dummy.next