# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    class DataObj:
        def __init__(self, mn, mx, is_bst):
            self.min = mn
            self.max = mx
            self.is_bst = is_bst

    def helper(self, root):

        # Base case
        if root is None:
            return self.DataObj(float('inf'), float('-inf'), True)

        left = self.helper(root.left)
        right = self.helper(root.right)

        # Calculate min and max for current subtree
        mn = min(left.min, root.val, right.min)
        mx = max(left.max, root.val, right.max)

        # BST conditions
        c1 = left.is_bst and right.is_bst
        c2 = left.max < root.val
        c3 = right.min > root.val

        is_bst = c1 and c2 and c3

        return self.DataObj(mn, mx, is_bst)

    def isValidBST(self, root):
        result = self.helper(root)
        return result.is_bst