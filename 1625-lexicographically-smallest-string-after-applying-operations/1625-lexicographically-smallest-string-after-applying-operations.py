from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        q = deque([s])
        smallest = s
        n = len(s)
        
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            
            # Update smallest
            if curr < smallest:
                smallest = curr
            
            # Operation 1: add a to odd indices
            s_list = list(curr)
            for i in range(1, n, 2):
                s_list[i] = str((int(s_list[i]) + a) % 10)
            added = ''.join(s_list)
            
            # Operation 2: rotate right by b
            rotated = curr[-b:] + curr[:-b]
            
            # Add new states
            q.append(added)
            q.append(rotated)
        
        return smallest
