class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case = length of root = 1 
        # left subtree = max length 
        # right subtree = max length 
        # recursive = root base + max ( maxDepth(left), maxDpeth(right))
        if not root:
            return 0

        max_length = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return max_length



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# #recurisive dfs 
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         #base case 
#         if not root:
#             return 0 
        
#         #adding 1 for root, then checking in left and right subtree, whoever's depth is more is added
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# #if we want to use iterative dfs for some reason 
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         stack = [[root,1]] #since we're at root, it's depth is 1 
#         res = 1 #since we're at depth 1 
#         while stack:
#             node, depth = stack.pop() # keep track of the node and its depth
#             if node:
#                 res = max(res,depth) #maximum of itself and depth, core of dfs
#                 #add those to stack  
#                 stack.append([node.left,depth+1])
#                 stack.append([node.right,depth+1])
#         return res


# #bfs 
# #i am thinking we can keep count of the levels, however many level, that's our max depth
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         level = 0 #no levels yet 
#         if not root:
#             return 0
        
#         q = deque([root]) #queue with root as level 1 
#  #while q is not emptly 
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft() #remove that node 
#                 #if it's children exists then add those to queue 
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right) 
#             # each time we remove parent and add it's children it's a new level, so we increment it 
#             level += 1
#         return level

