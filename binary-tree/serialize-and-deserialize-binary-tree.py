# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # serialization = conv obj/ds to bits sotred in memory
    # no restriction on how it works 
    # bt ser in string and deser into og tree
    # example = 1,2,3, null,null,4,5
    # about traversal = pre order, post order, in order 

    # use pre order traversal 
    # root -> recrusive left sub tree -> recrsive right sub tree
    # use comma as delimiter 
    # special value N for null tree 
    # pre order = 1,2,N,N,3,4,N,N,5,N,N (since 2, 4, and 5 has no children)
    # to create a new tree use pre order 
    # turn string into array by removing the delimiter comma 
    # first element is root 
    # how do we kno when left subtree stops and right sub tree begins 
    # whenever we see N, that sub tree is done, now next value if right node of val prev than N
    # base case in N, if we get two N, that subtree is done 
    # time = O(n) because only going through each node once 

    def serialize(self, root):
        res = []

        #run pre order recursively in the tree
        def dfs(node):
            #base case 
            if not node:
                res.append("N")
                return 
            res.append(str(node.val)) # since node value is int convert it to string 
            # run dfs on left subtree then right subtree
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        # join the array with delimiter comma 
        return ",".join(res)        

    def deserialize(self, data):

        #split the data with delimiter comma 
        vals = data.split(",")
        # global index to go over the string 
        self.i = 0

        # recruvise function to run preordr traversal on string 
        def dfs():
            #if its a null node 
            if vals[self.i] == "N":
                self.i +=1
                return 
            
            node = TreeNode(int(vals[self.i])) #since it's initially a string 
            #increment index since its used now 
            self.i +=1
            node.left = dfs()
            node.right = dfs()
            return node 

        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))