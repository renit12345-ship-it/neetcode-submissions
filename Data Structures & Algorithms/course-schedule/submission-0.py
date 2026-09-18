class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = defaultdict(list)
        for cs, pre in prerequisites:
            coursemap[cs].append(pre)
        visit = set()
        def dfs(cs):
            if cs in visit:
                return False
            if coursemap[cs] == []:
                return True 
            visit.add(cs)
            for pre in coursemap[cs]:
                if not dfs(pre):
                    return False
            visit.remove(cs)
            coursemap[cs] == []
            return True 
        for crs in range(numCourses):
            if not dfs(crs):
                return False 
        return True
            


        