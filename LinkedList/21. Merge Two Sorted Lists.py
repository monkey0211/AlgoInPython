# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node and head point to this dummy
        dummy = ListNode(0)
        head = dummy 
        if not list1: return list2
        if not list2: return list1
    
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                head = head.next
                list2 = list2.next
            else:
                head.next = list1
                head = head.next
                list1 = list1.next
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next
        return dummy.next # always return dymmy.next
        
        