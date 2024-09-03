# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        high=-999999999999999999
        self.nodes=0
        def dfs(high,curr):
            if(curr==None):
                return 0
            if(curr.val>=high):
                print(curr.val,"highh")
                self.nodes=self.nodes+1
                high=curr.val
            dfs(high,curr.right)
            dfs(high,curr.left)
        dfs(high,root)
        return self.nodes



        
