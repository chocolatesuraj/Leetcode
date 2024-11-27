# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None and list2==None):
            return None
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(lists)
        if(lists==[]):
            a=ListNode()
            a.val=None
            return 
        soln=[]
        for l in lists:
            soln=self.mergeTwoLists(soln,l)
        return soln
        
