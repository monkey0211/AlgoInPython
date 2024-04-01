# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        carry = 0
        sum = 0

        if not l1:
            return l2
        if not l2: 
            return l1
        while l1 or l2:  #这里是or的关系
            n1 = l1.val if l1 else 0 #没有的时候用0 不能用l1.val了
            n2 = l2.val if l2 else 0
            num = n1 + n2 + carry
            carry = num // 10 #
            node = ListNode(num % 10)
            curr.next = node
            curr = curr.next

            if l1: 
                l1 = l1.next
         
            if l2: 
                l2 = l2.next
        #最后还会剩carry!!
        if carry: 
            curr.next = ListNode(carry)
        return dummy.next