# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

    
        def maxDepth(curr):
            
            if not curr:
                return 0

            self.res = max(self.res, maxDepth(curr.left) + maxDepth(curr.right))

            return 1 + max(maxDepth(curr.left), maxDepth(curr.right))

        maxDepth(root)
        return self.res
            