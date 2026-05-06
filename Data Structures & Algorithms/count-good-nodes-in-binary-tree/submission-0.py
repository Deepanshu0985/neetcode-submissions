# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = []
        def roottonode(root,node,arr):
            if not root:
                return False
            arr.append(root.val)
            
            if root==node:
                return True
            
            right = roottonode(root.right,node,arr)
            left = roottonode(root.left,node,arr)

            if right or left :
                return True
            arr.pop()
            return False

        def helper(root):
            if not root:
                return 
            nodes.append(root)
            helper(root.right)
            helper(root.left)


        helper(root)
        ans = 0
        for node in nodes:
            temp = []
            roottonode(root,node,temp)
            if node.val>=max(temp):
                ans+=1
        
        return ans


        