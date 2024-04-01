# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time: O(n) space O(1)
# 1. split into two lists 2. reverse 2nd half list. 3. compare
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True

        secondhead = self.getSecondList(head)
        second = self.reverse(secondhead)

        while head and second:
            if head.val != second.val:
                return False
            head = head.next
            second = second.next
        return True
    def reverse(self, head):
        pre, head = None, head
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    def getSecondList(self, head):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.next #slow is end of the 1st half

