# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp=head
        count=0
        while(temp.next!=None):
            temp=temp.next
            count=count+1
        print(count)
        mid=int(count/2)+1
        temp=head
        for i in range(0,mid):
            prev=temp
            temp=temp.next
        prev.next=None
        #rint(head)
        #print("middd")
        #print(temp)
        prev=None
        oldtemp=temp
        while(temp!=None):
            oldtemp=temp
            newtemp=temp.next
            temp.next=prev
            prev=temp
            temp=newtemp
        #print(oldtemp)
        one=head
        two=oldtemp
        i=0
        while(one and two):
            i=i+1
            newone=one.next
            newtwo=two.next
            two.next=one.next
            one.next=two
            one=newone
            two=newtwo



        
