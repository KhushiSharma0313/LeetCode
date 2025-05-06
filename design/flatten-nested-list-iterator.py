# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # approach 
    # initilizases iterator 
    # next integrer in nested list 
    # true if some int in nested list 
    # example = [1,1], 2, [1,1]
    # layer of nested is arbitray
    # it has recusrive nature 
    # go forward, and go through entire list whenver you see a list 
    # each list decomposed into its children
    # recursive tree 
    # base case = integer
    # recruvse case = list 
    # time = O(n) iterating through each element 
    # memoery = O(n) making copy of list 
    def __init__(self, nestedList: [NestedInteger]):
        # to store the integer/ flattened values 
        self.stack = []
        #helper function to recursively go over each element i nested list 
        self.dfs(nestedList)
        # to get accees to next values we'll reverse the stack
        self.stack.reverse()
        
        
    
    def next(self) -> int:
        # popping the top value of stack since we've reversed it 
        return self.stack.pop()
        
    
    def hasNext(self) -> bool:
        return len(self.stack) >0

    def dfs(self, nested):
        for n in nested: 
        #iterate through each element in list 
        # base case 
            if n.isInteger():
            #add it to stack 
                self.stack.append(n.getInteger())

        #n is a list 
            else:
            # run dfs on it again 
                self.dfs(n.getList())
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())