class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = defaultdict(list)
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adjlist[u].append(v)
            indegree[v]+=1
        queue = deque(i for i in range(numCourses) if indegree[i]==0)
        before = [set() for _ in range(numCourses) ]
        while queue:
            node = queue.popleft()
            for p in adjlist[node]:
                before[p].add(node)
                before[p] |= before[node]
                indegree[p]-=1
                if indegree[p] == 0:
                    queue.append(p)
        return [u in before[v] for u, v in queries]

        