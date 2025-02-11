class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    # TC : O(1)
    # SC : O(n)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cachedict = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.tail.prev = self.head
        self.head.next = self.tail
    
    def movetofront(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.addtofront(node)
    
    def addtofront(self,node):
        nextnode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextnode
        nextnode.prev = node
    
    def removenode(self):
        if len(self.cachedict) > 0:
            nodetoremove = self.tail.prev
            del self.cachedict[nodetoremove.key]
            nodetoremove.prev.next = self.tail
            self.tail.prev = nodetoremove.prev
        

    def get(self, key: int) -> int:
        if key not in self.cachedict:
            return -1
        node = self.cachedict[key]
        self.movetofront(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if len(self.cachedict) == self.capacity:
            self.removenode()
        newnode = Node(key,value)
        self.cachedict[key] = newnode
        self.addtofront(newnode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)