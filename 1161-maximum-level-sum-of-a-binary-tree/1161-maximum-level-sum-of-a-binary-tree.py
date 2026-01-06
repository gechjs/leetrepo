# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        dic = dict()

        def dfs(node, level):
            dic[level] = dic.get(level, 0)+node.val
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)
            
        dfs(root, 1)
        
        smallest_level = 1
        maxval = root.val

        for key, val in dic.items():
            if maxval<val:
                maxval = val
                smallest_level = key
            elif maxval == val:
                smallest_level = min(smallest_level, key)
        return smallest_level


