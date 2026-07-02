class ListNode:
    def __init__(self, key = None, val = 0, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = ListNode()
        self.dummy.prev = self.dummy
        self.dummy.nxt = self.dummy
        self.mp = {}
        

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        else:
            node = self.mp[key]
            
            self.delete(node)
            self.addOnTop(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.delete(node)
            self.addOnTop(node)
        else:
            node = ListNode(key = key, val = value)
            self.mp[key] = node
            self.addOnTop(node)
        if len(self.mp) > self.capacity:
            del self.mp[self.dummy.prev.key]
            self.delete(self.dummy.prev)
            

    def delete(self, node):
        pre = node.prev
        pre.nxt = node.nxt
        node.nxt.prev = pre

    def addOnTop(self, node):
        nxt_node = self.dummy.nxt
        self.dummy.nxt = node
        node.prev = self.dummy
        node.nxt = nxt_node
        nxt_node.prev = node        
