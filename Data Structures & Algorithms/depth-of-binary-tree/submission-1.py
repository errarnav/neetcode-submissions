# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def goDeep(node, curHeight):
            nonlocal res
            if not node:
                return

            curHeight += 1
            res = max(res, curHeight)

            goDeep(node.left, curHeight)
            goDeep(node.right, curHeight)

            return

        goDeep(root, 0)

        return res