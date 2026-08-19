class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res1 = []
        for x,y in points:
            res = x**2 + y**2
            heapq.heappush(heap,[res,x,y])
        for _ in range(k):
            maxsa,x1,y1, = heapq.heappop(heap)
            res1.append([x1,y1])
        return res1


        