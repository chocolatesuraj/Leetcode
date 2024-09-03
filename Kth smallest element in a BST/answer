# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if(root.left==None and root.right==None):
            return root.val
        self.num=k
        self.res=0
        st=[]
        st.append(root)
        while(len(st)!=0):
            pr=[x.val for x in st]
            print(pr)
            if(st[-1].left!=None):
                st.append(st[-1].left)
            else:
                curr=st.pop()
                if(len(st)>=1):
                    st[-1].left=None
                print(curr)
                self.num=self.num-1
                if(self.num==0):
                    return curr.val
                if(curr.right!=None):
                    st.append(curr.right)





            
            



        
