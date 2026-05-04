class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        list1 = []
        list2 = []

        def roottonodepath(root, key, arr):
            if not root:
                return False

            arr.append(root)

            if root.val == key.val:   # changed here
                return True

            if roottonodepath(root.left, key, arr) or roottonodepath(root.right, key, arr):
                return True

            arr.pop()
            return False

        roottonodepath(root, p, list1)
        roottonodepath(root, q, list2)

        ans = None
        i = 0

        while i < len(list1) and i < len(list2):
            if list1[i].val == list2[i].val:
                ans = list1[i]
            else:
                break
            i += 1

        return ans