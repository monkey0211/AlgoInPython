# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # two path: 1) get list length. 2) remove node
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        
        length = 0
        while head: 
            length += 1
            head = head.next
        n = length + 1 - n

        head = dummy
        for _ in range(n-1):
            head = head.next

        head.next = head.next.next
        return dummy.next




        