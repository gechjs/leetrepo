# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total  , MOD =  0 , 10**9 + 7
        def compute_total(node):
            nonlocal total
            if not node:
                return
            total += node.val
            compute_total(node.left)
            compute_total(node.right)
        compute_total(root)
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            nonlocal total
            if not node:
                return 0
            if not node.left and not node.right:
                ans = max(ans , node.val * (total - node.val ))
                return node.val
            node_sum = dfs(node.left ) + dfs(node.right) + node.val
            ans = max(ans , node_sum * (total - node_sum))
            return node_sum
        dfs(root)
        return ans % MOD
            
                