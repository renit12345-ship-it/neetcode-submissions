class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            # BASE CASE 1: Out of bounds or water = 1 perimeter edge! (You nailed this)
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return 1 
            
            # BASE CASE 2: Already visited land = 0 perimeter edges
            if (r, c) in visit:
                return 0
                
            # Mark as visited (NO removing it later!)
            visit.add((r, c))
            
            count = 0 
            # Explore all 4 directions and sum up the edges they find
            count += dfs(r+1, c)
            count += dfs(r, c+1)
            count += dfs(r-1, c)
            count += dfs(r, c-1)
            
            return count 

        # The "Satellite Scanner"
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # The problem states there is exactly ONE island.
                    # So the moment we find it and calculate it, just return the answer!
                    return dfs(r, c)
