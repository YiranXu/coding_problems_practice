class linkedqueue:
    class _Node:
        def __init__(self,data,next_):
            self.data=data
            self.next=next_
        
    def __init__(self):
        self.head=None 
        self.tail=None
        self.size=0
    def enqueue(self,val):
        """add to the end"""
        new=self._Node(val,None)
        if self.size==0:
            self.head=new
        else:
            self.tail.next=new
        self.tail=new
        self.size+=1
    def dequeue(self):
        """remove the front(first) of the queue"""
        if self.size==0:
            return False 
        answer=self.head.data
        self.head=self.head.next
        self.size-=1
        if self.size==0:
            self.tail=None
        return answer
class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.queue=linkedqueue()
        self.prev_sum=0
    def next(self, val: int) -> float:
        new=self.queue.enqueue(val)
        tail=self.queue.dequeue() if self.queue.size>self.size else 0
        new_sum=self.prev_sum-tail+val
        self.prev_sum=new_sum
        return new_sum/self.queue.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
if __name__=='__main__':
    orders=["MovingAverage","next","next","next","next"]
    inputs=[[3],[1],[10],[3],[5]]

    obj = MovingAverage(inputs[0][0])
    result=[]
    for i in range(1,len(inputs)):
        param=obj.next(inputs[i][0])
        print(param)
        result.append(param)