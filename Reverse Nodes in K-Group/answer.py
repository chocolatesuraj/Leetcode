# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k==1):
            return head
        initbeg=head
        newbeg=None
        cur=head
        prev=None
        newloop=ListNode()
        isstart=True
        end=False
        while(cur):
            temp=cur
            for i in range(k):
                if(temp):
                    temp=temp.next
                else:
                    end=True
                    return newbeg
            print(end)
            if(end==False):
                for i in range(k):
                    
                    if(cur):
                        print(cur.val)
                        newcur=cur.next
                        (cur.next)=prev
                        prev=cur
                        oldcur=cur
                        cur=newcur
                if(isstart==True):
                    newbeg=oldcur
                    isstart=False

                newloop.next=oldcur
                newloop=initbeg
                initbeg.next=cur
                initbeg=cur
                print("newloop",newloop,"\ninitbeg",initbeg)
            
            #break
        return newbeg
        
        
