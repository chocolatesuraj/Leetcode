# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(q==None  and p==None):
            return True 
        elif(q==None  or p==None):
            return False
        if (q.val != p.val):
            return False
        
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
