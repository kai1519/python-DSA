class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None) or (head.next.next == None):
            return head
        
        start1 = start2 = end1 = end2 = None
        count = 1
        
        while head:
            temp = head
            head = head.next
            temp.next = None
            
            if count % 2:
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
            
            count += 1
        
    
        end1.next = start2
        
        return start1