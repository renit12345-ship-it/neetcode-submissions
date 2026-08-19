class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        
        while maxheap and len(maxheap) > 1:

            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            if x < y:
                heapq.heappush(maxheap,x-y)
            elif y > x:
                heapq.heapppush(maxheap,y-x)
        heapq.heappush(maxheap,0)
        return abs(maxheap[0])


