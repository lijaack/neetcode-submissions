# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False
            if root.val == subRoot.val:
                sub = self.isSameTree(root,subRoot)
                if sub:
                    return sub
            left = dfs(root.left)
            right = dfs(root.right)
            return left or right
             

        return dfs(root)

    def isSameTree(self, left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val: 
            leftCheck = self.isSameTree(left.left,right.left)
            rightCheck = self.isSameTree(left.right, right.right)
            return leftCheck and rightCheck
        return False
