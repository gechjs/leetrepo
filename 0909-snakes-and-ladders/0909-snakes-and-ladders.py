class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        MAX = n * n
        q = deque([1])
        visited = [False] * (MAX + 1)
        visited[1] = True
        
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                
                if curr == MAX:
                    return level
                
                for next_pos in range(curr + 1, min(curr + 6, MAX) + 1):
                    dest = next_pos
                    # Calculate board position
                    row = (next_pos - 1) // n
                    col = (next_pos - 1) % n
                    if row % 2 == 1:  # Odd rows are right-to-left
                        col = n - 1 - col
                    
                    row = n - 1 - row  # Convert to board coordinates
                    
                    if board[row][col] != -1:
                        dest = board[row][col]
                    
                    if not visited[dest]:
                        visited[dest] = True
                        q.append(dest)
            level += 1
        return -1