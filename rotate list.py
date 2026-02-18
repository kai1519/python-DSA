# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        Re = k % count
        if Re == 0:
            return head

        temp = head
        ind = (count - Re) - 1

        while ind:
            temp = temp.next
            ind -= 1

        tm = temp.next
        temp.next = None
        temp = tm

        while temp.next:
            temp = temp.next

        temp.next = head
        return tm