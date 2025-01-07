class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while len(self.q1)>1:
            self.q2.append(self.q1.pop(0))
        popped = self.q1.pop(0)
        self.q1, self.q2 = self.q2,[]
        return popped    

    def top(self) -> int:
        while len(self.q1)>1:
            self.q2.append(self.q1.pop(0))
        topped = self.q1[0]
        self.q2.append(self.q1.pop(0))
        self.q1,self.q2 = self.q2, []
        return topped    
        

    def empty(self) -> bool:
        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()