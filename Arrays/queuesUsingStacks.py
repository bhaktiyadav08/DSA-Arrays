class makeQueue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
    def push(self,x):
        self.in_stack.append(x)
    
    def pop(self,x):
        if not self.out_stack and self.in_stack:
            while self.in_stack:
                element=self.in_stack.pop()
                self.out_stack.append(element)
        return self.out_stack.pop()
    def peek(self):
        if self.out_stack:
          return self.out_stack[-1]
        elif self.in_stack:
            while self.in_stack:
                element=self.in_stack.pop()
                self.out_stack.append(element)
            return self.out_stack[-1]
        else:
            return[]
    def empty(self):
        if not self.in_stack and not self.out_stack:
            return True
    