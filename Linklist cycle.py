class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = head
        fp = head
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True
        
        return False
