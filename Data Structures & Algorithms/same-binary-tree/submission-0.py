# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.list_P =[]
        self.list_Q = []

        def dfs(curr, list1, position):
            if not curr:
                return None

            if not dfs(curr.left, list1, 'left') and not dfs(curr.right, list1, 'right'):
                # then we know its a leaf node
                if position == 'left':
                    list1.append(str(curr.val) + 'l')
                elif position == 'right':
                    list1.append(str(curr.val) + 'r')
                else:
                    list1.append(str(curr.val) + 'c')

            return None
        
        dfs(p, self.list_P, 'centre')
        dfs(q, self.list_Q, 'centre')

        return (self.list_P == self.list_Q)

            