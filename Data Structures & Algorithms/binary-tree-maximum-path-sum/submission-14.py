# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val

        def dfs(node):
            nonlocal max_path

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Best single path we can send upward
            curr_max_path = node.val + max(left, right, 0)

            # Best path through this node
            curr_max = node.val + max(left, 0) + max(right, 0)

            max_path = max(max_path, curr_max)

            return curr_max_path

        dfs(root)
        return max_path