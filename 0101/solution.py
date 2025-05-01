# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.h(root.left, root.right)
    
    def h(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return self.h(a.left, b.right) and self.h(a.right, b.left) and a.val == b.val