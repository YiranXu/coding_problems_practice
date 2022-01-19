class MinStack:
    #every elemnt in the stack is a tuple (value, current min)
    def __init__(self):
        self.min=float('inf') 
        self.stack=[]
        
    def push(self, val):
        if len(self.stack)==0:
            self.min=val
        else:
            self.min=self.getMin()
        if val<self.min:
            self.min=val
        self.stack.append((val,self.min))
        

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

if __name__ == "__main__":
    orders=["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    input=[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
    st=None
    for i in range(len(orders)):
        o=orders[i]
        inp=input[i]
        if o=='MinStack':
            st=MinStack()
            print('null')
        elif o=='push':
            st.push(int(inp[0]))
            print('null')
        elif o=='top':
            print(st.top())
        elif o=='pop':
            st.pop()
            print('null')
        elif o=='getMin':
            print(st.getMin())
