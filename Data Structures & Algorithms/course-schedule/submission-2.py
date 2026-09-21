class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for c,p in prerequisites: 
            adjlist[c].append(p)
        seen = set()
        def cycle(c,seen):
            if c in seen:
                return True
            seen.add(c)
            for p in adjlist[c]:
                if cycle(p,seen):
                    return True 
            seen.remove(c)
            adjlist[c] = []
            return False

        for c in range(numCourses):
            if  cycle(c,seen):
                return False
        return True
        