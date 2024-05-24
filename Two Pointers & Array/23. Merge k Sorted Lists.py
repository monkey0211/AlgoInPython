# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda x, y: (x.val < y.val)
# time O(nlogk)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        import heapq
        heap = []
        dummy = ListNode(0)
        node = dummy

        for head in lists:
            if head: #must have. 否则会把None加入heap, 后面h可能会是None type(no h.next)
                heapq.heappush(heap, head)
        
        while heap:
            h = heapq.heappop(heap)
            node.next = h
            node = node.next
            if h.next:
                heapq.heappush(heap, h.next)
    
        return dummy.next
        