class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heaps = nums
        self.k = k
        heapq.heapify(self.heaps)
        while len(self.heaps) > self.k:
            heapq.heappop(self.heaps)
        
    def add(self, val: int) -> int:

        heapq.heappush(self.heaps,val)
        while len(self.heaps) > self.k:
            heapq.heappop(self.heaps)
        return self.heaps[0]
        
