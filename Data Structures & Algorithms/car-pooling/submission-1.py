class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap = []
        tp=0
        trips.sort(key=lambda x:x[1])
        for t in trips:
            np,start,end = t
            while minheap and minheap[0][0] <= start:
                tp-=minheap[0][1]
                heapq.heappop(minheap)

            tp+=np
            heapq.heappush(minheap,[end,np])
            if tp > capacity:
                return False 
        return True
        