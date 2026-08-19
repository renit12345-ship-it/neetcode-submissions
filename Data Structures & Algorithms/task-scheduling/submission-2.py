class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxheap = [-count for count in counter.values()]
        heapq.heapify(maxheap)
        queue = deque()
        time = 0
        while maxheap or queue:
            time+=1
            if maxheap:
                count = heapq.heappop(maxheap)+1
                if count < 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                count,_ = queue.popleft()
                heapq.heappush(maxheap,count)
        return time 
        