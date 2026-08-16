# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 2 3 4 5 6 7 8 9 10
        # 1 10 2 9 3 8 4 7 5 6

        slow, fast = head, head.next

        # this places slow at the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondList = slow.next # this is the head of the second list
        slow.next = None # this severs the connection from the last elem of first   list to the first elem of second list

        # now reversing the second list
        prev = None
        cur = secondList

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        secondList = prev

        # now merging second list and first one

        first, second = head, secondList

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

