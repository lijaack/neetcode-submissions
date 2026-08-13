# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path=root.val

        def dfs(node):
            nonlocal max_path
            if not node:
                return
            curr_val = node.val
            curr_max=curr_val
            curr_max_path=curr_max
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            if left_val:
                curr_max = max(curr_max,curr_val + left_val)
                curr_max_path = max(curr_max,curr_val + left_val)
            if right_val:
                curr_max = max(curr_max,curr_val + right_val)
                curr_max_path = max(curr_max,curr_val + right_val)
            if left_val and right_val:        
                curr_max = max(curr_max, curr_val+right_val+left_val)
            max_path = max(curr_max, max_path)
            return curr_max_path
        dfs(root)
        return max_path
            
