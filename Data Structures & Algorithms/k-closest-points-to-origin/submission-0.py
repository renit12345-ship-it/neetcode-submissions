import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x, y in points:
            # Calculate x^2 + y^2
            dist = x**2 + y**2
            # Push the distance paired with the point
            heapq.heappush(min_heap, (dist, [x, y]))
            
        res = []
        # The top k elements popped are guaranteed to be the closest
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            res.append(point)
            
        return res