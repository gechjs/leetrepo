# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        total = 0

        def find_total(node):
            nonlocal total
            total += node.val

            if node.right:
                find_total(node.right)
            if node.left:
                find_total(node.left)

        find_total(root)
        ans = 1

        def dfs(node):
            nonlocal ans
            nonlocal total
            if not node.left and not node.right:
                ans = max(ans, node.val * (total - node.val))
                return node.val
            left_sum=0
            right_sum = 0
            if node.left:
                left_sum = dfs(node.left)
                ans = max(ans, left_sum * (total - left_sum))
            if node.right:
                right_sum = dfs(node.right)
                ans = max(ans, right_sum * (total - right_sum))
            return left_sum+right_sum+node.val
        dfs(root)

        return ans%(10**9+7)
