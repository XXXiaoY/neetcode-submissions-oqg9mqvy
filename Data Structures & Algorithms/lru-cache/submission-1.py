class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = ListNode()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.delete_node(node)
        self.add_node_to_top(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value

            self.delete_node(node)
            self.add_node_to_top(node)
            return

        node = ListNode(key, value)
        self.key_to_node[key] = node
        self.add_node_to_top(node)

        if len(self.key_to_node) > self.capacity:
            bottom_node = self.dummy.prev
            self.delete_node(bottom_node)
            del self.key_to_node[bottom_node.key]

    def add_node_to_top(self, node):
        first = self.dummy.next

        self.dummy.next = node
        node.prev = self.dummy

        node.next = first
        first.prev = node

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev