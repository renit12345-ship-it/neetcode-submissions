class MyQueue:

    def __init__(self):
        self.stack = []
        self.s2 = []
        

    def push(self, x: int) -> None:

        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.s2 :
            while self.stack:
                self.s2.append(self.stack.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2 :

            while self.stack:
                self.s2.append(self.stack.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:

        return max(len(self.stack),len(self.s2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()