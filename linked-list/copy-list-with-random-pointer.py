"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        curr = head 
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next 

        curr = head 
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next 
        
        return oldToCopy[head]

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         # time = O(n) # each pass is iterating through entire linked list 
#         # memory = O(n) hasmap takes that much mem 
#         # diff between this linked list is each node has extra pointer called random 
#         # create a deep copy of it 
#         # only tricky part is random pointer, so if nde is pointing to a another node that's not been create yet
#         # we'll do two passes, for it first pass if just creating copy of node itself 
#         # and create hasmap that maps og nodes to new nodes
#         # in second pass, we'll do all the pointer connecting 
#         # leverage the hashmap  to get pointer from og nodes and point them to copy nodes
#         # 
#         #hasmap to point old linked list to new 
#         oldToCopy = {None: None} #since linked list has a null node at the end 

#         #first pass = creating the nodes copy 
#         curr = head 
        
#         #until current node is not null
#         while curr: 
#             #create the node 
#             copy = Node(curr.val)
#             #map this to old node in hashmap 
#             oldToCopy[curr]= copy
#             #move on to new node 
#             curr = curr.next 
        
#         #second pass of pointing 
#         curr = head 
#         while curr: 
#             copy = oldToCopy[curr]
#             #next pointer same as old one in hashmap 
#             copy.next = oldToCopy[curr.next]
#             #random pointer same as old one in hashmap 
#             copy.random = oldToCopy[curr.random]
#             #move to new node
#             curr = curr.next 
        
#         return oldToCopy[head]
        