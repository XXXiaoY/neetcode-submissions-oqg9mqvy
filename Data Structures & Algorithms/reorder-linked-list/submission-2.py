# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        def findMid(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast  = fast.next.next
            return slow
        
        #merge
        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            cur.next = l1
            return dummy
        
        #reverse
        def reverse(head):
            prev = None
            cur = head
            while cur:
                nxt  = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        mid = findMid(head)
        head2 = mid.next
        mid.next = None
        re_head2 = reverse(head2)

        merge(head, re_head2)
        