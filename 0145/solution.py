# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        if not root: return
        self.dns(root)
        return self.ans

    def dns(self, node):
        if node.left:
            self.dns(node.left)
        if node.right:
            self.dns(node.right)
        self.ans.append(node.val)