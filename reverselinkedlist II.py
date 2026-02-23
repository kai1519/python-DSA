class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head
        temp = head
        count = 0
        p1End = p2End = p2Start = p3Start = None
        while temp:
            if count == (left - 2):
                p1End = temp
                p2Start = temp.next
                temp = temp.next
                p1End.next = None
            elif count == (right - 1):
                p2End = temp
                p3Start = temp.next
                temp = temp.next
                p2End.next = None
            else:
                temp = temp.next
            count += 1
            
        start = end = None
        if left == 1:
            p2Start = head
        while p2Start:
            temp = p2Start
            p2Start = p2Start.next
            if end == None:
                start = end = temp
                end.next = None
            else:
                temp.next = start
                start = temp
        if p1End:
            p1End.next = start
        else:
            head = start
        end.next = p3Start

        return head