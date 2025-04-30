# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case 
        if not root:
            return 0 
        
        #adding 1 for root, then checking in left and right subtree, whoever's depth is more is added
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))