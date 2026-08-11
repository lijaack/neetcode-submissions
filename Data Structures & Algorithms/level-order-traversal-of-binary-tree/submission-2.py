# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack =[root]
        stackTemp=[]

        res=[]
        resTemp=[]

        while stack:
            if stack[0].left:
                stackTemp.append(stack[0].left)
            if stack[0].right:   
                stackTemp.append(stack[0].right)
            if stack[0]:
                resTemp.append(stack[0].val)
            stack.pop(0)
            if not stack:
                res.append(resTemp)
                resTemp=[]
                stack.extend(stackTemp)
                stackTemp=[]
        return res


