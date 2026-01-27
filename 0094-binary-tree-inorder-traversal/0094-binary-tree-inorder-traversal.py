# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans
        def tree(node):
            nonlocal ans
            if node.left:
                tree(node.left)
            
            ans.append(node.val)

            if node.right:
                tree(node.right)
        
        tree(root)

        return ans
            