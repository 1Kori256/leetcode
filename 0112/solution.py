# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        self.dfs(root, 0, targetSum)
        return self.ans

    def dfs(self, root, s, target):
        if not root:
            return 
        s += root.val
        if not root.left and not root.right:
            if s == target:
                self.ans = True
        
        self.dfs(root.left, s, target)
        self.dfs(root.right, s, target)
