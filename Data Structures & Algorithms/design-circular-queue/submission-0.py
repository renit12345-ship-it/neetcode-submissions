class ListNode :
    def __init__(self,val,nxt=None,prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
    
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.space = k
        self.left = ListNode(0)
        self.right= ListNode(0,None,self.left)
        self.left.next = self.right
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value,self.right,self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space-=1
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space+=1
        return True
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.next.val
        else :
            return -1 
        
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.prev.val
        else :
            return -1 

    def isEmpty(self) -> bool:
        return self.space == self.k
        
    def isFull(self) -> bool:
        return self.space == 0