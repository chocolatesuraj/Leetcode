# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxval=-99999
        def func(node):
            if(node.left==None and node.right==None):
                if(node.val>self.maxval):
                    self.maxval=node.val
                return node.val
                
            right=-99999
            left=-99999
            val=node.val
            if(node.right!=None):
                right=func(node.right)
            if(node.left!=None):
                left=func(node.left)
            sol=max(val+right,val,val+left,val+right+left)
            if(sol>self.maxval):
                self.maxval=sol
            retsol=max(val+right,val,val+left)
            return retsol
        func(root)
        return self.maxval
    
        
