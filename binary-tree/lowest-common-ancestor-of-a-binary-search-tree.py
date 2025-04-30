# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #for bst l < root < r
        # for lca, in case of 2 and 8, it was 6 becuase both were in different sub trees
        # or one of them is root 
        # or one of them is parent and other is child
        #point is whenever they're not in same subtree, we can find lca 
        #start at the root, since it's common ancestor to all 
        #move down, then check if elements are in same subtree or diff by comparing it to root 

        #pointer to move from node to node in tree, start at root 
        curr = root 

        #go through each node,so until curr is null
        while curr:
            #when both nodes in left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            #when both nodes in right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #when both node in diff subtree, or one of them is parent to other, or one of them is root 
            else:
                return curr
        return 




        