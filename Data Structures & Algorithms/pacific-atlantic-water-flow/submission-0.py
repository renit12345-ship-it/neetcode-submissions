class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW,COL = len(heights),len(heights[0])
        pac,atl = set(),set()
        def dfs(r,c,visit,prevHeight):
            if r < 0 or c < 0 or (r,c) in visit or r == ROW or c == COL or prevHeight > heights[r][c]:
                return  
            visit.add((r,c))
            check = [(-1,0),(0,1),(1,0),(0,-1)]
            for dr,dc in check:
                nr,nc = dr+r, dc+c 
                dfs(nr,nc,visit,heights[r][c])
                

            
        for c in range(COL):
            dfs(0,c,pac,heights[0][c])
            dfs(ROW-1,c,atl,heights[ROW-1][c])
        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,atl,heights[r][COL-1])
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl :
                    res.append([r,c])
        return res
        