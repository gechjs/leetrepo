class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(curr, adj, visited, longest, colors):
            if visited[curr] == 1:  # Cycle found
                return float('inf')
            
            if visited[curr] == 0: 
                visited[curr] = 1
                for nbr in adj[curr]:
                    res = dfs(nbr, adj, visited, longest, colors)
                    if res == float('inf'):
                        return float('inf')
                    
                    for i in range(26):
                        longest[i][curr] = max(longest[i][curr], longest[i][nbr])
                longest[ord(colors[curr]) - ord('a')][curr] += 1
                visited[curr] = 2
            return longest[ord(colors[curr]) - ord('a')][curr]

        n = len(colors)
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])

        longest = [[0] * n for _ in range(26)]
       
        max_color_length = 0
        visited = [0] * n
    
        for i in range(n):
            res = dfs(i, adj, visited, longest, colors)
            if res == float('inf'):
                return -1
            max_color_length = max(max_color_length, res)
        return max_color_length