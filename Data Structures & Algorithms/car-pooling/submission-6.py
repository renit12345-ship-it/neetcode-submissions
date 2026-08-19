class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        totalpass = 0
        heap = []
        for t in trips:
            np, start,end = t
            while heap and heap[0][0] <= start:
                totalpass-= heap[0][1]
                heapq.heappop(heap)

            totalpass+=np
            heapq.heappush(heap,[end,np])
            if totalpass > capacity:
                return False 
        return True