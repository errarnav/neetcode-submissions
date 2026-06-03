# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    #===========================================================================================

        cur1 = l1
        cur2 = l2
        length1 = 0
        length2 = 0

        while cur1:
            length1 += 1
            cur1 = cur1.next

        while cur2:
            length2 += 1
            cur2 = cur2.next

        cur1 = l1
        if length1 < length2:
            for i in range(length2 - 1):
                if not cur1.next:
                    cur1.next = ListNode(val = 0)
                
                cur1 = cur1.next

        cur2 = l2
        if length1 > length2:
            for i in range(length1 - 1):
                if not cur2.next:
                    cur2.next = ListNode(val = 0)
                
                cur2 = cur2.next
                
    #===========================================================================================

        

        curr1 = l1
        curr2 = l2
        carry = 0
        elem = 0

        while curr1 and curr2:
            if elem == 0:
                new_head = ListNode()
                new = new_head
            else:
                new.next = ListNode()
                new = new.next

            val1 = curr1.val
            val2 = curr2.val

            total = val1 + val2 + carry
            if total <= 9:
                new.val = total
                carry = 0

            else:
                carry = 1
                new.val = total - 10

            

            curr1 = curr1.next
            curr2 = curr2.next
            elem += 1
        
        if carry == 1:
            new.next = ListNode(val = 1)

        return new_head


        