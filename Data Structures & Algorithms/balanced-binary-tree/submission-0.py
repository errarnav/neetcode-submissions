# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = 0

        def maxDepth(curr):
            if not curr:
                return 0

            left_depth = maxDepth(curr.left)
            right_depth = maxDepth(curr.right)

            if abs(right_depth - left_depth) > 1:
                self.res += 1
            
            return 1 + max(left_depth, right_depth)

        
        maxDepth(root)
        if self.res > 0:
            return False
        else:
            return True

            

            

        