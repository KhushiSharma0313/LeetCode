# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#bfs 
#i am thinking we can keep count of the levels, however many level, that's our max depth
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0 #no levels yet 
        if not root:
            return 0
        
        q = deque([root]) #queue with root as level 1 
 #while q is not emptly 
        while q:
            for i in range(len(q)):
                node = q.popleft() #remove that node 
                #if it's children exists then add those to queue 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            # each time we remove parent and add it's children it's a new level, so we increment it 
            level += 1
        return level

# #recurisive dfs 
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         #base case 
#         if not root:
#             return 0 
        
#         #adding 1 for root, then checking in left and right subtree, whoever's depth is more is added
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))