# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True

        def dfs(curr):
            print(self.res)
            if(curr==None):
                return 0
            
            r= 1+dfs(curr.right)
            l= 1+dfs(curr.left)
            print(curr.val,r,l)
            if(r-l>1 or l-r>1):
                self.res=False
            return max(r,l)
        dfs(root)
        return self.res

        
        
