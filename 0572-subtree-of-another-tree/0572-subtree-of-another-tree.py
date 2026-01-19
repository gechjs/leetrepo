# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(nodeLeft, nodeRight):
            if not nodeLeft and nodeRight or not nodeRight and nodeLeft:
                return False
            if not nodeLeft and not nodeRight:
                return True
            if nodeLeft.val != nodeRight.val:
                return False
            if check(nodeLeft.left, nodeRight.left) and check(nodeLeft.right, nodeRight.right):
                return True
            return False
        def dfs(node):
            if not node:
                return False
            if check(node, subRoot):
                return True

            if dfs(node.right) or dfs(node.left):
                return True
            return False
        
        return dfs(root)