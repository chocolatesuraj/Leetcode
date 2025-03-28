# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root==None:
            #min max bool 
            return [+999999999999,-999999999999999,True]
        else:
            minr, maxr , validr= self.dfs(root.right)
            minl, maxl , validl= self.dfs(root.left)
            # print(root.val,minl,maxr)
            # print(min(minr,minl),max(maxr,maxl),validr and validl and 
            #  minl> root.val and maxr<root.val )
            return (min(minr,min(minl,root.val)),max(maxr,max(maxl,root.val)),validr and validl and 
             maxl< root.val and minr>root.val )

    def isValidBST(self,root):
        return self.dfs(root)[2]
        
