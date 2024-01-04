class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
        

    def pop(self):
        for _ in range(len(self.input)):
            self.output.append(self.input.pop())
        
        last = self.output.pop()
                       
        for _ in range(len(self.output)):
            self.input.append(self.output.pop())
        return last
                       
    def peek(self):
        return self.input[0]      

    def empty(self):
        return len(self.input) == 0    
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()