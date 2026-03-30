"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                # 要复制的 random 是 cur.random 的下一个节点
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 删除交错链表中的原链表节点，剩下的节点即为新链表
        if not head: return None
        cur = head
        new_head = head.next
        while cur:
            copy = cur.next        # 找到对应的新节点
            cur.next = copy.next   # 【关键】恢复原链表的指向 (老1 -> 老2)
            cur = cur.next         # 老指针后移
            
            if cur:
                copy.next = cur.next # 【关键】建立新链表的指向 (新1 -> 新2)
            else:
                copy.next = None     # 新链表到头了
                
        return new_head

        