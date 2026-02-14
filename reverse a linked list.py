from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        while head:
            temp = head
            head = head.next

            temp.next = p
            p = temp
        return p