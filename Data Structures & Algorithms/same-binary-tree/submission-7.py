# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val: 
            leftCheck = self.isSameTree(left.left,right.left)
            rightCheck = self.isSameTree(left.right, right.right)
            return leftCheck and rightCheck
        return False