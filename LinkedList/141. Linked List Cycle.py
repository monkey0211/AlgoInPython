# 看是否有环 快慢指针 如果有环 两指针一定在环里相遇
# time O(n) space O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
       
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: 
                return True
        return False
