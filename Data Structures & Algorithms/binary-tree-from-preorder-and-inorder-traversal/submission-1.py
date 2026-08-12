# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        # Store each value's position in inorder.
        # This lets us find the root's position instantly
        # instead of searching through inorder every time.
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Keeps track of which value in preorder we should use next.
        self.pre_idx = 0

        def dfs(l, r):
            # No values in this range = no subtree
            if l > r:
                return None

            # Preorder is ROOT → LEFT → RIGHT,
            # so the next unused preorder value is always
            # the root of the current subtree.
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # Create the root node
            root = TreeNode(root_val)

            # Find where this root is located in inorder.
            # Everything to the left belongs to the left subtree.
            # Everything to the right belongs to the right subtree.
            mid = indices[root_val]

            # Build the left subtree using the portion of
            # inorder that is to the left of the root.
            root.left = dfs(l, mid - 1)

            # Build the right subtree using the portion of
            # inorder that is to the right of the root.
            root.right = dfs(mid + 1, r)

            # Return the completed subtree to the parent
            return root

        # Initially, the entire inorder array is available
        # to build the whole tree.
        return dfs(0, len(inorder) - 1)