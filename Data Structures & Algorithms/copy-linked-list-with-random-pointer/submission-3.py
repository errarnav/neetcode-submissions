"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}
        
        cur = head

        while cur:
            oldToNew[cur] = Node(x = cur.val)
            cur = cur.next

        cur = head

        while cur:
            newNode = oldToNew[cur]
            newNode.next = oldToNew[cur.next] # to set next
            newNode.random = oldToNew[cur.random] # to set random
            cur = cur.next

        return oldToNew[head]



