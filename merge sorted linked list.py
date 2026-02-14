class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        s = e = None
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
                temp.next = None
                if s == None:
                    s = e = temp
                else:
                    e.next = temp
                    e = temp
            else:
                temp = l2
                l2 = l2.next
                temp.next = None
                if s == None:
                    s = e = temp
                else:
                    e.next = temp
                    e = temp
        if l1:
            if s == None:
                s = l1
            else:
                e.next = l1
        elif l2:
            if s == None:
                s = l2
            else:
                e.next = l2
        return s