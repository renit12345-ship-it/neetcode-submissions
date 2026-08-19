class ListNode:
    def __init__(self, key=0, value=0): # Give them defaults
        self.key = key       # Bug: typo 'sef.key = 0' ignores input
        self.value = value   # Bug: 'self.value = 0' ignores input
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev =self.left
        self.cache = {}
        self.track = 0
        
    def insert(self,node):
        temp1= self.right.prev
        temp1.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = temp1
        self.track+=1

    def remove(self,node):
        prevnode,nextnode = node.prev , node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        self.track-=1


        
    def get(self, key: int) -> int:

        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = ListNode(key,value)
            self.insert(self.cache[key])
        else :
            self.cache[key] = ListNode(key,value)
            self.insert(self.cache[key])

        if self.cap < self.track:
            lru_node = self.left.next     # 1. Grab the node next to left dummy
            self.remove(lru_node)         # 2. Chop it out of the linked list
            del self.cache[lru_node.key]  # 3. Completely delete it from the hashmap!

