# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        prev=ListNode()
        head=prev
        while (l1 or l2):
            if(l1):
                val1=l1.val
            else:
                val1=0
            if(l2):
                val2=l2.val
            else:
                val2=0
            total= val1+val2+carry
            if(total>=10):
                carry=  math. floor(total/10)
                total=total%10
            else:
                carry=0
            new=ListNode()
            new.val=total
            prev.next=new
            prev=new
            if(l1):
                l1=l1.next
            if(l2):
                l2=l2.next
        if(carry!=0):
            new=ListNode()
            new.val=carry
            prev.next=new
        return head.next
            
