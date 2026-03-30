class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = ListNode()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

        

    def get(self, key: int) -> int:
        if key not in self.key_to_node:  # 没有这本书
            return -1
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放到最上面
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.remove(node)
            self.push_front(node)
            return
        else:
            node = ListNode(key, value)
            self.key_to_node[key] = node
            self.push_front(node)
            if len(self.key_to_node) > self.capacity:  # 书太多了
                back_node = self.dummy.prev
                del self.key_to_node[back_node.key]
                self.remove(back_node)  # 去掉最后一本书



        

    def remove(self, x: ListNode) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def push_front(self, x: ListNode) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)