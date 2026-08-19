class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxheap = [[-cnt,char] for char,cnt in counts.items()]
        heapq.heapify(maxheap)
        prev = None
        res = ""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt,chr1 = heapq.heappop(maxheap)
            res+=chr1
            cnt+=1
            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,chr1]
        return res 
        