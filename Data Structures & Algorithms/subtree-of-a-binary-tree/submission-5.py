# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(a,b):
            if not a and not b:
                return True
            if (a and not b) or (not a and b):
                return False
            if a.val == b.val and sametree(a.left, b.left) and sametree(a.right, b.right):
                return True
            return False
        if not root:
            return False 
        if not subRoot:
            return True
        return sametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)