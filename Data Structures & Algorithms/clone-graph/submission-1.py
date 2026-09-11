"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visit = set()
        oldToNew = {}
        def dfs(cur):
            if cur in visit:
                return oldToNew[cur]

            oldToNew[cur] = Node(cur.val)
            visit.add(cur)

            for neigh in cur.neighbors:
                newNeigh = dfs(neigh)
                if newNeigh not in oldToNew[cur].neighbors:
                    oldToNew[cur].neighbors.append(newNeigh)

            return oldToNew[cur]

        if not node:
            return None
        return dfs(node)
        


            



