# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,head: Optional[ListNode]) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self,head: Optional[ListNode]) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head1 = self.findMid(head)
        head2 = head1.next
        head1.next = None

        head2 = self.reverse(head2)
        dummy = head
        
        while head2:
            nxt1 = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt1
            
            head = nxt1
            head2 = nxt2
        
     
        
        