class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0
        queue = deque()
        while queue or maxheap:
            time+=1
            if maxheap:
                res = heapq.heappop(maxheap)+1
                if res:
                    queue.append([res,time+n])
            if queue and time == queue[0][1]:
                heapq.heappush(maxheap,queue.popleft()[0])
        return time