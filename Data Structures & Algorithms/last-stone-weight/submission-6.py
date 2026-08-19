class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)
        while len(stone) > 1:
            a = heapq.heappop(stone)
            b = heapq.heappop(stone)
            if a < b:
                heapq.heappush(stone,(a-b))
            else:
                heapq.heappush(stone,(b-a))
            
        return abs(stone[0])
        