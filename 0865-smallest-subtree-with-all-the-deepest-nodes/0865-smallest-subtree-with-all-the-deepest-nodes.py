# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        dic = defaultdict(set)

        def dfs(node, level):
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
            
            if not node.left and not node.right:
                dic[level].add(node.val)
        dfs(root, 0)

        deepest = max(dic)
        ans = root
        flag = True
        def find_subtree(node):
            nonlocal ans, flag, deepest
            if not node.right and not node.left:
                if len(dic[deepest])==1 and node.val in dic[deepest]:
                    ans = node
                    flag = False
                return 1 if node.val in dic[deepest] else 0
            left, right = 0, 0
            if node.left:
                left = find_subtree(node.left)
            if node.right:
                right = find_subtree(node.right)
            
            if flag and left+right == len(dic[deepest]):
                ans = node
                flag = False

            return left+right
   
        find_subtree(root)

        return ans
