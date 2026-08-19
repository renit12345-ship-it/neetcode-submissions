class ListNode :
    def __init__(self,key=0,val=0,next = None, prev = None):

        self.val,self.next,self.prev = val,next,prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left,self.right = ListNode(), ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def insert(self,node):
        curr = node
        prev_node , next_node =self.right.prev, self.right
        curr.next = next_node 
        curr.prev = prev_node 
        prev_node.next = curr
        next_node.prev = curr
    
    def remove(self, node):
        prev_node , next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def get(self, key: int) -> int:
        if key in self.cache :

            temp = self.cache[key]
            self.remove(temp)
            self.insert(temp)
            return temp.val
        return -1 

        
        

    def put(self, key: int, value: int) -> None:
        # 1. If key already exists, delete the old node version out of the tracks
        if key in self.cache:
            self.remove(self.cache[key])
            
        # 2. Create the node with BOTH key and value, then insert it
        curr = ListNode(key, value) 
        self.cache[key] = curr
        self.insert(curr)
        
        # 3. Check if we went over capacity
        if len(self.cache) > self.cap:
            # Grab the oldest node (right after the left wall)
            lru_node = self.left.next
            
            # Evict it completely from both tracking systems
            self.remove(lru_node)
            del self.cache[lru_node.key]
            


        
