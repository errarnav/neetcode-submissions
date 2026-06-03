# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            return head.next

        node_to_stop_at = length - n + 1

        curr = head
        node_index = 1
        prev = None
        while node_index < node_to_stop_at:
            prev = curr
            curr = curr.next
            node_index += 1

        if prev == None:
            head = curr.next
        else:
            prev.next = curr.next

        return head


        

        