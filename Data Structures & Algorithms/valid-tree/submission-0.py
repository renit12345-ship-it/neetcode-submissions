class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for src,des in edges:
            adjlist[src].append(des)
            adjlist[des].append(src)
        visit = set()
        def dfs(i,prev):
            if i in visit:
                return False 
            visit.add(i)
            for p in adjlist[i]:
                if p == prev:
                    continue
                if not dfs(p,i):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n
        