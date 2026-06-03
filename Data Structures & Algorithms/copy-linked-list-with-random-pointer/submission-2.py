

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        if not head:
            return None

        k = 0 # k = length
        curr = head
        while curr:
            k += 1
            curr = curr.next

    

        loc = {}
        tracker = head
        new_headd = Node(tracker.val)
        new_head = new_headd
        for i in range(k):
            if i == k - 1:
                new_head.val = tracker.val
            else:
                # new_head.val = tracker.val
                new_head.next = Node(tracker.next.val)

            loc[tracker] = new_head

            new_head = new_head.next
            tracker = tracker.next

        curr = new_headd
        og = head
        for i in range(k):
            
            
            addy = og.random
            if addy:
                new_addy = loc[addy]
                curr.random = new_addy
            else:
                curr.random = None

            og = og.next
            curr = curr.next

        return new_headd


