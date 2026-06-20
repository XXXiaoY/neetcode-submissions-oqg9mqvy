# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2:
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            v = add % 10
            node = ListNode(v)
            cur.next = node
            cur = cur.next
            add = add // 10
        
        if add:
            cur.next = ListNode(add)


        return dummy.next

        