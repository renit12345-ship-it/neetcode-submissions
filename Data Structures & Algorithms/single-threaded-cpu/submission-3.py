class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x: x[0])
        minheap,res,time,i = [],[],0,0
        heapq.heapify(minheap)
        while i < len(tasks) or minheap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minheap,(tasks[i][1],tasks[i][2]))    
                i+=1 
            if minheap:
                proctime,index = heapq.heappop(minheap)
                time+=proctime
                res.append(index)
            else:
                time = tasks[i][0]
        return res