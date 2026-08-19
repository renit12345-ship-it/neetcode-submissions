class Node :
    def __init__(self,key,val):

        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def remove(self,node):
        prv,nxt = node.prev,node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self,node):

        prv,nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next ,node.prev = nxt,prv


    def get(self, key: int) -> int:
        if key in self.cache :
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap :
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
