class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n =3, 3 open and 3 closed 
        # rule = "(" =")" = n
        # for every open there needs to be a closed
        # so when inserting closed -> it cam't go in the start it needs to have open parenthese already 
        # moment they get paired we pop them 
        # ((( )))-> (-> () or (( 
            # you can insert close when close < = open 
            # insert open, when open <= n 
        #whenever there's valid pop them out 
        stack =[]
        res = [] #containing the resulting parenthese 

        def backtrack(openN, closeN):
            # valid parentheses
            if openN == closeN == n:
                res.append("".join(stack))

            # insert open 
            if openN < n:
                stack.append("(")
                backtrack(openN +1, closeN)
                stack.pop()

            #insert close 
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN +1)
                stack.pop()

        #eventually both open and close parentheses is 0
        backtrack(0,0)
        return res

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # well formed = valid parenthese 
#         # n = including both parenthese 
#         # brute force 
#         # n =3 
#         # 3 open and 3 closed 
#         # order = start out with open, open count should match closed count then remove it from stack 
#         # for adding open parenthese -> open count < n 
#         # only add close para -> close count < open count 
#         # stop when open = close = n
#         # for each parenthese we have 2 coices, to add or not to add based on above condtions 
        
#         #stack and list 
#         stack = []
#         res = []

#         # helper function to backtrack 
#         def backtrack(openN, closeN):
#             if openN == closeN == n:
#                 #add the parentheses from stack to result list 
#                 res.append("".join(stack))
#                 return  

#             # if open parentheses is less than total count, ad it to stack 
#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closeN) 
#                 stack.pop()

#             # if close is less than open, it's valid parentheses, add it to stack 
#             if closeN < openN:
#                 stack.append(")")
#                 backtrack(openN, closeN +1) 
#                 stack.pop()
        
#         backtrack(0,0)
#         return res

        