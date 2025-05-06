class MinStack:

    def __init__(self):
        self.stack = []
        #keeping track of min values
        self.minStack = []
        # initilizses stack object
        #push function pushes val onto stack 
        # pop removes value on top of stack 
        # top gets top element of stack 
        # getMins retrieves min element in stack constant time 

        # use built in data strucure 
        # everything stack can do apart fron getMin 
        # brute force is look through each element = O(n)
        # look at current minimum value for each element 
        # so we'll have another stack with minimum value 
        # so whenever pushing/popping we'll do it in both stacks to keep track of min 
        # for getMin, look at top of min stack 
        # implement stack with list 


        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #for min stack, determine which val is min, the val itself or top val of stack 
        # val = min(val, self.minStack[-1] if self.minStack else val)
        # self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        # self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return top value of min stack 
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()