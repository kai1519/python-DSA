class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp = head
        sp = head
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        return sp
