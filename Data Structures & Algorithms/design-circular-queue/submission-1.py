class ListNode:

    def __init__(self,value = 0,next = None,prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.left,self.right = ListNode(),ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp1 = self.right.prev
        newnode = ListNode(value)
        temp1.next = newnode
        newnode.prev = temp1
        newnode.next = self.right
        self.right.prev = newnode
        self.size+=1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        temp1 = self.left.next.next
        self.left.next = self.left.next.next
        temp1.prev = self.left
        self.size-=1
        return True
        
        

    def Front(self) -> int:

        if self.isEmpty():
            return -1 
        return self.left.next.value
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1 
        return self.right.prev.value
        

    def isEmpty(self) -> bool:

        return  self.left.next == self.right
        

    def isFull(self) -> bool:

        return self.size == self.cap
        

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()