# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            
            next_one_for_slow = slow.next
            slow = next_one_for_slow

            next_one_for_fast_is_two_ahead = fast.next.next
            fast = next_one_for_fast_is_two_ahead

            if slow == fast:
                return True
        
        return False