from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        visit = set()    # finished courses, already in output
        path = set()     # courses on the current DFS path
        adjlist = defaultdict(list)
        for c, p in prerequisites:
            adjlist[c].append(p)

        def cycle(c):
            if c in path:
                return True
            if c in visit:
                return False
            path.add(c)
            for p in adjlist[c]:
                if cycle(p):
                    return True
            path.remove(c)
            visit.add(c)
            output.append(c)
            return False

        for c in range(numCourses):
            if cycle(c):
                return []

        return output