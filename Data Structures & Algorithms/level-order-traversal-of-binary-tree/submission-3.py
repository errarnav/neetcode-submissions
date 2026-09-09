# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                Node = q.popleft()
                if Node:
                    level.append(Node.val)
                    if Node.left:
                        q.append(Node.left)
                    if Node.right:
                        q.append(Node.right)
            
            if level:
                res.append(level)

        return res