class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)
        while len(self.heap) > 1:
            first = heapq.heappop(self.heap)
            second = heapq.heappop(self.heap)
            if first < second:
                heapq.heappush(self.heap,(first-second))
        
        heapq.heappush(self.heap,0)
        return abs(self.heap[0])
        