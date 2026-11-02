# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            a = max(dfs(node.left),0)
            b = max(dfs(node.right),0)
            res[0] = max(a+b+node.val, res[0])
            return max(a+node.val, b+node.val)

        dfs(root)
        return res[0]