# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currHigh):
            if not node:
                return 0
            totalGood=0
            if(node.val >= currHigh):
                totalGood += 1
            currHigh = max(node.val, currHigh)
            left = dfs(node.left,currHigh)
            right = dfs(node.right, currHigh)
             
            return totalGood +left + right
        return dfs(root,float("-inf"))