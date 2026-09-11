class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        time = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                check = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in check:
                    nr,nc = dr+r , c+dc
                    if nr < 0 or nc < 0 or nr == m or nc == n or grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1

        

        