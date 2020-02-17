"""
@Author:    Hai Nguyen
@Date:      Nov 4th, 2019
@Source:    AlgoPro
@Task:      Determine a binary tree is a valid binary search tree.
@Desc:      Assume a BST is defined as follows:
            The left subtree of a node contains only nodes with keys that are less than that of the node's key.
            The right subtree of a node contains only nodes with keys that are greater than that of the node's key.
            Both the left and right subtree must also be binary search tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def IsValidBST(self, root):
        def Helper(node, lower, upper):
            #base case, if a node is null, still a valid BST
            if not node:
                return True
            #get the value of current node
            val = node.val
            #Check the current node with its direct children
            if val <= lower or val >= upper:
                return False
            #Recursively check the right subtree
            if not Helper(node.right, val, upper):
                return False
            #Recursively check the left subtree
            if not Helper(node.left, lower, val):
                return False
            #At this point, all failure tests are passed 
            #Thus, the BST with this current node must be valid
            return True
        #At the root node, we don't care about lower, upper limits
        #Just apply infinities
        return Helper(root, float('-inf'), float('inf'))
    
#Test 01
#It should return True
#node = TreeNode(5)
#node.left = TreeNode(1)
#node.right = TreeNode(7)
#rightNode = node.right
#rightNode.left = TreeNode(6)
#rightNode.right = TreeNode(8)

#Test 02
#It should return False
node = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(6)
rightNode = node.right
rightNode.left = TreeNode(4)
rightNode.right = TreeNode(7)

print(Solution().IsValidBST(node))