# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root,left,right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            
            right_ans = helper(root.right ,root.val,right)
            left_ans = helper(root.left ,left,root.val)

            return right_ans and left_ans
        return helper(root,float('-inf'),float('inf'))

        