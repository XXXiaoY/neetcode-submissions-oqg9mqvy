# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = cur = ListNode()
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))
        while heap:
            val, index, p = heapq.heappop(heap)
            if p.next:
                heapq.heappush(heap,(p.next.val,index,p.next))
            cur.next = p
            cur = cur.next
        return dummy.next
            
        
        