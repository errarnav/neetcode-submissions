# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = ListNode(next = head)

        # counting the total number of elements in the list

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        
        targetIndex = length - n

        cur = head
        prev = res

        for i in range(length):
            if i == targetIndex:
                nxtNode = cur.next
                # cur.next = None
                prev.next = nxtNode
                break
            
            tmp = cur.next
            prev = cur
            cur = tmp
        
        return res.next




        



        


        