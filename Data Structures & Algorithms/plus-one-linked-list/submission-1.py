# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sent = ListNode(0,next = head)
        non_nine = sent 
        while head:
            if head.val!=9:
                non_nine = head
            head = head.next
        non_nine.val+= 1 
        non_nine = non_nine.next

        while non_nine:
            non_nine.val = 0
            non_nine = non_nine.next

        return sent if sent.val != 0 else sent.next