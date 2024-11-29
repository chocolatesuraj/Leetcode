# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(self.isSameTree(root,subRoot)):
            return True
        if(root==None):
            return False
        elif(root!=None):
            return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(q==None  and p==None):
            return True 
        elif(q==None  or p==None):
            return False
        if (q.val != p.val):
            return False
        
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
