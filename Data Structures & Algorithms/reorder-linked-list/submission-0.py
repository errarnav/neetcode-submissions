# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next or not head.next.next:
            return

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head

        for _ in range(len(stack) // 2):
            last_elem = stack.pop()
            second_elem = cur.next
            cur.next = last_elem
            last_elem.next = second_elem
            cur = second_elem

        cur.next = None
            