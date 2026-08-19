class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= []
        res = []
        for nums in points:
            start,end = nums
            first = start**2
            second = end**2
            heapq.heappush(heap,(first+second,start,end))
        while k:
            a,b,c =heapq.heappop(heap)
            res.append((b,c))
            k-=1
        return res