# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.solution=None
        self.checknum(root, p.val, q.val)
        return self.solution
         
    def checknum(self,node,a,b)->[bool,bool]:# chcecks if numbeers are 
        ans= [False,False]
        if(node==None):
            ans= [False,False]
            return ([False,False])
        elif(node.val==a):
            ans=[True,False]
        elif(node.val==b):
            ans= [False,True]
        
        i=self.checknum(node.left,a,b) 
        j=self.checknum(node.right,a,b)
        temp= [a or b for a, b in zip(i, j)]
        print(i,j,temp)
        print("tempp",temp)
        k= [a or b for a, b in zip(temp, ans)]
        if(k ==[True,True]):
            print(node.val) 
            if(self.solution==None):
                self.solution=node
        print(k, node.val)
        return k

        

        
