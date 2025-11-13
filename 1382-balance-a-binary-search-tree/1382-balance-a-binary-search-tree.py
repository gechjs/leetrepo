# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_vals = inorder(root)
        
        def build_balanced(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_vals[mid])
            node.left = build_balanced(left, mid - 1)
            node.right = build_balanced(mid + 1, right)
            return node
        
        return build_balanced(0, len(sorted_vals) - 1)
