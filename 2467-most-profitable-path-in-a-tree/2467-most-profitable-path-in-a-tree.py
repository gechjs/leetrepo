class Solution:
    def findBobPath(self, adj: List[List[int]], bob: int, parent: int, curr_path: List[int], bob_path: List[int]) -> bool:
        if bob == 0:
            bob_path.extend(curr_path)
            bob_path.append(0)
            return True
        curr_path.append(bob)
        for neighbor in adj[bob]:
            if neighbor != parent and self.findBobPath(adj, neighbor, bob, curr_path, bob_path):
                return True
        curr_path.pop()
        return False

    def findMaxIncomeForAlice(self, adj: List[List[int]], alice: int, parent: int, amount: List[int]) -> int:
        max_income = float('-inf')
        is_leaf = True

        for neighbor in adj[alice]:
            if neighbor != parent:
                is_leaf = False
                income = self.findMaxIncomeForAlice(adj, neighbor, alice, amount)
                max_income = max(max_income, income)

        return amount[alice] if is_leaf else amount[alice] + max_income

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        bob_path = []
        self.findBobPath(adj, bob, -1, [], bob_path)

        path_len = len(bob_path)
        for i in range(path_len // 2):
            amount[bob_path[i]] = 0
        if path_len % 2 == 1:
            amount[bob_path[path_len // 2]] //= 2

        return self.findMaxIncomeForAlice(adj, 0, -1, amount)
