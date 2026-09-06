# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(cur):
            if not cur:
                return
            
            temp = cur.right
            cur.right = cur.left
            cur.left = temp

            reverse(cur.left)
            reverse(cur.right)

            return

        reverse(root)
        return root

