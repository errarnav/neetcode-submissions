# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        list1 = []
        list2 = []
        
        def dfs(node):
            if not node:
                list1.append('null')
                return

            list1.append(node.val)

            dfs(node.left)
            dfs(node.right)

            return

        dfs(p)

        def dfs(node):
            if not node:
                list2.append('null')
                return

            list2.append(node.val)

            dfs(node.left)
            dfs(node.right)

            return

        dfs(q)
        
        print(list1, list2)
        return list1 == list2

            