class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        island = 0
        visit = set()
        def bfs(r,c):
            queue = deque([(r,c)])
            while queue:
                cr,cc = queue.popleft()
                check = [(0,1),(1,0),(-1,0),(0,-1)]
                for dc, dr in check:
                    nr,nc = (cr+dr),(cc+dc)
                    if nr < 0 or nc < 0 or nr == n or nc == m or grid[nr][nc] == "0" or (nr, nc) in visit:
                        continue
                    visit.add((nr,nc))
                    queue.append((nr,nc))


        
        

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r,c) not in visit :
                    bfs(r,c)
                    island+=1
        return island



        

        