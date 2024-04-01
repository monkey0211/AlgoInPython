# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head

        ptr = dummy # 必须从dummy开始(not dummy.next), 不然会溢出, 导致lpre.next不存在
        for _ in range(left-1):
            ptr = ptr.next
        lpre = ptr
       
        ptr = dummy
        for _ in range(right):
            ptr = ptr.next
        r = ptr
    
        rpro = r.next
        r.next = None
        l = lpre.next     
        lpre.next = self.reverse(l)
        l.next = rpro
        return dummy.next

    def reverse(self, head):
        prev, head = None, head
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
