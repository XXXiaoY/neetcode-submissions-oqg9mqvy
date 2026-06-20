import heapq
from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        cur = dummy

        idx = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, idx, node))
                idx += 1
        
        while heap:
            val, _, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
                idx += 1
        
        return dummy.next