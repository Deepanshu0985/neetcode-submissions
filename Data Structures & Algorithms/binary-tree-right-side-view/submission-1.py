class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        q = [root]

        while q:
            s = len(q)
            res = 0

            for i in range(s):
                node = q.pop(0)

                res = node.val  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(res)

        return ans