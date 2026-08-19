class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node to protect the head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 2. Advance 'right' n times to create the gap
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 3. Move both pointers together until 'right' hits the end (None)
        while right:
            left = left.next
            right = right.next
            
        # 4. Now 'left' is right before the target node. Delete it!
        left.next = left.next.next
        
        # Return the actual starting head
        return dummy.next