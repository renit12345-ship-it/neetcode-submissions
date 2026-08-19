class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1,l2 = list1,list2 
        dummy = ListNode()
        res = dummy
        while l1 and l2 :
            if l1.val >= l2.val :
                res.next = l2
                l2= l2.next
            else :
                res.next = l1
                l1= l1.next
            res = res.next 
        if l1:
            res.next = l1
        if l2 :
            res.next = l2
        return dummy.next