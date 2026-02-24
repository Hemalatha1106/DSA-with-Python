class MinStack:

    def __init__(self):
        self.st=[]
        self.mnst=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mnst or self.mnst[-1] >= val:
            self.mnst.append(val)

    def pop(self) -> None:
        if self.mnst[-1]==self.st[-1]:
            self.mnst.pop()
        return self.st.pop()    

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mnst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()