# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def fun(root):
            if root:
                right = root.right
                root.right = fun(root.left)
                root.left = fun(right)
            return root

        fun(root)
        return root