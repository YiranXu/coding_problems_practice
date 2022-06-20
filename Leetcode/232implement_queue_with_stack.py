class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x: int) -> None:
        self.stack_in.append(x)
    
    def pop(self) -> int:
        if self.empty():
            return
        if self.stack_out:
            return self.stack_out.pop()
        else:   
            while len(self.stack_in)!=0:
                x=self.stack_in.pop()
                self.stack_out.append(x)
            return self.stack_out.pop()
    def peek(self) -> int:
        ans=self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not(self.stack_in or self.stack_out)

if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_0 = obj.pop()
    obj.push(3)
    param_2 = obj.pop()
    param_2 = obj.empty()
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()