# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp=ListNode()
        temp.next=head
        curr=head
        prev=temp
        
        for i in range(left-1):
            curr=curr.next
            prev=prev.next

        store=prev
        curr=curr.next
        prev=prev.next
        store.next=None
        prev.next=None
        store_rotate=prev

        for i in range(right-left):
            newcurr=curr.next
            curr.next=prev
            prev=curr
            curr=newcurr

        store.next=prev
        store_rotate.next=curr

        return temp.next
            


            
