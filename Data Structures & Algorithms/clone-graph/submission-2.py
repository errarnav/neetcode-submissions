"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        def dfs(cur):
            if cur in oldToNew:
                return oldToNew[cur]

            clone = Node(cur.val)
            oldToNew[cur] = clone

            for neigh in cur.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone

        if not node:
            return None
        return dfs(node)
        


            



