class MyCircularQueue:

    def __init__(self, k: int):
        self.length=k
        self.queue=[[]]*self.length
        self.head=0
        self.tail=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.queue[self.head]=value
            else:
                if self.tail==self.length-1:
                    self.tail=0
                else:
                    self.tail+=1 
                self.queue[self.tail]=value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head]=[]
            self.head+=1
            return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue[self.head]==[]:
            self.head=0
            self.tail=self.head
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.head+self.tail==self.length-1:
            return True
        else:
            return False

if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(2)
    param_1 = obj.enQueue(1)
    param_2 = obj.enQueue(2)
    param_3 = obj.deQueue()
    param_4 = obj.enQueue(3)
    param_5 = obj.deQueue()
    param_7 = obj.enQueue(3)
    param_8 = obj.deQueue()
    param_9 = obj.enQueue(3)
    param_10 = obj.deQueue()
    param_11 = obj.Front()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()