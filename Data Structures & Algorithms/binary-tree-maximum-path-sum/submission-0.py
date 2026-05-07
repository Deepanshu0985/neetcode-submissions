# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = float('-inf')

        def helper(root):
            nonlocal maxval
            if not root:
                return 0 
            leftmax = max(0,helper(root.left))
            rightmax = max(0,helper(root.right))

            maxval = max(maxval,(root.val +leftmax+rightmax))

            return root.val + max(leftmax,rightmax)
        helper(root)
        return maxval
        