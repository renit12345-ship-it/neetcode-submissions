class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = head 
        Leftprev = dummy
        for _ in range(left-1):
            tmp = curr
            curr = curr.next
            Leftprev = tmp
        prv = None 
        for _ in range((right - left)+1):
            tmp = curr.next
            curr.next = prv
            prv = curr
            curr = tmp
        Leftprev.next.next = curr
        Leftprev.next = prv
        return dummy.next