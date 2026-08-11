# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)

            # -1 means the left subtree is already unbalanced.
            if left == -1:
                return -1

            right = dfs(root.right)

            # -1 means the right subtree is already unbalanced.
            if right == -1:
                return -1

            # If the two subtree heights differ by more than 1,
            # this subtree is unbalanced.
            if abs(left - right) > 1:
                return -1

            # Return this subtree's height to its parent.
            return 1 + max(left, right)

        return dfs(root) != -1