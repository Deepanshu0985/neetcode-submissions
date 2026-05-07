# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.ans = -1

        def inorder(root):

            if not root:
                return

            inorder(root.left)

            self.count += 1

            if self.count == k:
                self.ans = root.val
                return

            inorder(root.right)

        inorder(root)

        return self.ans