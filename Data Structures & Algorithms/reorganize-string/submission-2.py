class Solution:
    def reorganizeString(self, s: str) -> str: 
        prev = None 
        res = ""
        counters = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in counters.items()]
        heapq.heapify(maxheap)
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            cnt, char = heapq.heappop(maxheap)
            cnt += 1
            res += char
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res