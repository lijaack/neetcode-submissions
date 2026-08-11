# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]

        q=deque([root])

        while q:
            qlen=len(q)

            for i in range(qlen):
                if i == qlen-1:
                        res.append(q[0].val)
                if q[0].left: 
                    q.append(q[0].left)
                if q[0].right: 
                    q.append(q[0].right)
                q.popleft()
        return res 

