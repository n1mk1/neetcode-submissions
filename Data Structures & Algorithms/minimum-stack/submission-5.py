# stack datastructure
class MinStack:
    # Constructor
    def __init__(self):
        self.stack = []
        self.minstack = []
    # push
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)          
    # pop
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()    
    # top
    def top(self) -> int:
        return self.stack[-1]
    # getMin
    def getMin(self) -> int:
        return self.minstack[-1] 
