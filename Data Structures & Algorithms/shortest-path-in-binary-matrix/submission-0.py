class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = set()
        visited.add((0,0))
        queue = deque([(0,0)])
        length = 1
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == n-1 and c == m-1:
                    return length
                check = [(-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
                for dr,dc in check:
                    nr,nc = r+dr,c+dc
                    if nr < 0 or nc < 0 or nr == n or nc == m or grid[nr][nc] == 1 or (nr,nc) in visited:
                        continue
                    visited.add((nr,nc))
                    queue.append((nr,nc))
            length+=1
        return -1
