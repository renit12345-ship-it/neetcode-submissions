from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque()
        
        # 1. The Scanner: Find all treasures and put them in the queue immediately
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # 2. Multi-Source BFS (The "Rot" spreading outward)
        while queue:
            r, c = queue.popleft()
            check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for dr, dc in check:
                nr, nc = r + dr, c + dc
                
                # If out of bounds, OR if it's a wall (-1), OR if it's already been visited/is a treasure... skip it!
                if nr < 0 or nc < 0 or nr == m or nc == n or grid[nr][nc] != 2147483647:
                    continue
                    
                # We found an unvisited empty room! 
                # Its shortest distance is exactly 1 step further than the cell we are standing on.
                grid[nr][nc] = grid[r][c] + 1
                
                # Add this newly discovered room to the queue so it can spread distance to its neighbors
                queue.append((nr, nc))
