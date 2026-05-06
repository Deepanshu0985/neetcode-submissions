# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,maxval):
            if not root:
                return 0 
            res = 1 if root.val>=maxval else 0
            maxval = max(root.val,maxval)
            res+=helper(root.right,maxval)
            res+=helper(root.left,maxval)
            return res
        
        return helper(root,root.val)
        