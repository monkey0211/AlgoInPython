#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head

        fast, slow = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHead = slow.next
        slow.next = None

        second = self.reverse(secondHead)
        first = dummy.next
    
        self.mergeLists(first, second)
      
    def reverse(self, node):
        prev, node = None, node
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev
    #这里要求in-place merge. 所以不能新创建一个list
    def mergeLists(self, first, second):
        while first and second:
            tmp1 = first.next  
            first.next = second
            first = tmp1    
           
            tmp2 = second.next
            second.next = first
            second = tmp2


