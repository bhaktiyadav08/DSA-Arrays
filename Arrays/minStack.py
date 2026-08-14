class minstack:
    
    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.minimum=float('inf')
    def push(self,value):
        self.stack.append(value)
        curr_minimum=value
        if curr_minimum<=self.minimum:
            self.minimum=curr_minimum
            self.minstack.append(self.minimum)

    def pop(self):
        self.stack.pop()
        
    

    def getMin(self):
        return self.minstack[-1]
        


    

