class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        seen = set()

        graph = defaultdict(list)
        if source==destination:
            return True
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(arr):
            nonlocal seen
            for ele in arr:
                if ele == destination:
                    return True
                if ele not in seen:
                    seen.add(ele)
                    dfs(graph[ele])
            return False
        return dfs(graph[source])