# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:

        # Both p and q are smaller → go left.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both p and q are larger → go right.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise, they split at this node,
        # or one of them IS this node.
        return root