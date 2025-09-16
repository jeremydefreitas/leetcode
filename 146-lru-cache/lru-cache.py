class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.lu = Node(0, 0)
        self.mu = Node(0, 0)

        self.lu.next = self.mu
        self.mu.prev = self.lu

    
    def insert(self, node):
        oldRecent = self.mu.prev

        node.prev = oldRecent
        oldRecent.next = node
        self.mu.prev = node
        node.next = self.mu
        

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev  

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.lu.next
            self.remove(lru)
            del self.cache[lru.key]

        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)