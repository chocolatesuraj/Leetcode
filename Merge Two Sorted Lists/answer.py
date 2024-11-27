# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c=ListNode()
        head=c
        a=list1
        b=list2
        while(a and b):
            if(a.val<b.val):
                c.next=a
                c=c.next
                a=a.next
            elif(a.val>=b.val):
                c.next=b
                c=c.next
                b=b.next
        
        if(a):
            c.next=a
        if(b):
            c.next=b

        return head.next
            

        
