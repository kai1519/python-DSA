class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        
        ha = headA
        hb = headB
        
        while ha:
            d[ha] = -1
            ha = ha.next
        
        while hb:
            if hb in d:
                return hb
            hb = hb.next
        
        return None
