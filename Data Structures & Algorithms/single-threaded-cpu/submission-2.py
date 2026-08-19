class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x:x[0])
        minheap = []
        res = []
        time = i = 0
        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                # Push [Processing Time, Original Index] to the heap
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minheap:
                time = tasks[i][0]
            else:
                proctime,index = heapq.heappop(minheap)
                time+=proctime
                res.append(index)
        return res
