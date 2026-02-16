class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        P = head
        while P:
            if P.next != None and P.val == P.next.val:
                temp = P.next
                P.next = temp.next
                temp.next = None
            else:
                P = P.next
        return head