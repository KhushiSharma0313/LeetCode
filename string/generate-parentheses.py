class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # well formed = valid parenthese 
        # n = including both parenthese 
        # brute force 
        # n =3 
        # 3 open and 3 closed 
        # order = start out with open, open count should match closed count then remove it from stack 
        # for adding open parenthese -> open count < n 
        # only add close para -> close count < open count 
        # stop when open = close = n
        # for each parenthese we have 2 coices, to add or not to add based on above condtions 
        
        #stack and list 
        stack = []
        res = []

        # helper function to backtrack 
        def backtrack(openN, closeN):
            if openN == closeN == n:
                #add the parentheses from stack to result list 
                res.append("".join(stack))
                return  

            # if open parentheses is less than total count, ad it to stack 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN) 
                stack.pop()

            # if close is less than open, it's valid parentheses, add it to stack 
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN +1) 
                stack.pop()
        
        backtrack(0,0)
        return res

        