# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        def dfs(curr):
            print(self.res)
            if(curr==None):
                return 0
            
            r= dfs(curr.right)
            l= dfs(curr.left)
            print(curr.val,r,l)
            if(r+l>self.res):    
                self.res=r+l
            print("r,l",r,l)
            return 1+max(r,l)
        dfs(root)
        return self.res

        
