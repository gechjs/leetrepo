# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr, ans = 1, 0
        def dfs(node):
            nonlocal ans, curr
            if node.left:
               dfs(node.left)
            
            if curr==k:
                ans = node.val
            curr+=1
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans
        
            