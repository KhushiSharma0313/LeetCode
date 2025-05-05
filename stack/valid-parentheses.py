class Solution:
    def isValid(self, s: str) -> bool:
        # time = O(n)
        # memory = O(n)
        # number of both typ of bracket should be equal 
        # it's order should be correct
        # start with open bracket and end with closing bracket 
        # the moment a parentheses match, we can remove it from consideration 
        # if we have empty list by the end, it's true
        # helpful to use a stack here, since we'll remove last in first out order 
        #  how do we match parantheses
        # use hashmap to match opening bracket and closing bracket 
        # if stack is empty true
         
        # stack for adding and popping parentheses
        stack = []
        #hashmap to map close and open parentheses
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        #iterate through the string 
        for c in s:
            # if this is closed parentheses
            if c in closeToOpen:
                # if it's in empty stack, or if it's open parenthese already exists
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            # if it's open parenthese 
            else:
                stack.append(c)

        # if stack is empty its true
        return True if not stack else False



        