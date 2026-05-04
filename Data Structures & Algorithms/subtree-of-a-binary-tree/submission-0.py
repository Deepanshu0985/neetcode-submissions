class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return helper(p.left, q.left) and helper(p.right, q.right)

        def find(root, subRoot):
            if not root:
                return False
            
            if helper(root, subRoot):
                return True
            
            return find(root.left, subRoot) or find(root.right, subRoot)

        return find(root, subRoot)