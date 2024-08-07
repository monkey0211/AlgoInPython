# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 先把所有的head都放入heap, while heap挨个pop, pop出来的如果有下一个就接着push to heap. 
# node move to next. 
# 必须要写comparator: 
ListNode.__lt__ = lambda x, y: (x.val < y.val)

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
        