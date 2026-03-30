# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        dummy = ListNode(next = head)
        p0 = dummy
        prev = None
        cur = p0.next
        while n >= k:
            n -= k 
            for i in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            next_p0 = p0.next
            p0.next.next = cur
            p0.next = prev
            p0 = next_p0

        return dummy.next
        