class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head == None or x < -100 or x > 100:
            return head
        
        start1 = end1 = None
        start2 = end2 = None
        
        while head:
            temp = head
            head = head.next
            temp.next = None
            
            if x > temp.val:
                if start1 == None:
                    start1 = end1 = temp
                else:
                    end1.next = temp
                    end1 = temp
            else:
                if start2 == None:
                    start2 = end2 = temp
                else:
                    end2.next = temp
                    end2 = temp
        
        if start1 and start2:
            end1.next = start2
            return start1
        
        if start1:
            return start1
        
        return start2