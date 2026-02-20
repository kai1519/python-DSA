class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        p = tm = head.next
        start = end = None
        temp = tm = None
        
        while head != None and head.next != None:
            if head.val == head.next.val or head.val == (temp and temp.val):
                temp = head
                head = head.next
            else:
                tm = temp = head
                head = head.next
                tm.next = None
                if start == None:
                    start = end = tm
                else:
                    end.next = tm
                    end = tm
        
        if head != None and head.val != (temp and temp.val):
            if start == None:
                return head
            else:
                end.next = head
        
        return start