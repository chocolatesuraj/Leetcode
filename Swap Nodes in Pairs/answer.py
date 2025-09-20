# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start=ListNode()
        start.next=head
        prev=start
        first=head 
        newfirst=first
        while(first and first.next):

            second=first.next
            # print("first",first.val,"second",second.val)
            newfirst=second.next 

            prev.next=second
            second.next=first
            prev=first
            first.next=None
            first=newfirst
            # print("first",first.val,"second",second.val,"prev",prev.val)
        # return 0
        prev.next=newfirst
        return start.next
        
