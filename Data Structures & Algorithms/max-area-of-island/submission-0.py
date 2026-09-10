class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = set()
        max_area = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r == n or c == m or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 or (r,c) in visited:
                    continue
                area = dfs(r,c)
                max_area = max(max_area, area)
        return max_area
        