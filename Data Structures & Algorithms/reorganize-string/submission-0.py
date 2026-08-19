import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Count frequencies of each character
        count = Counter(s) # e.g., {"a": 3, "b": 1}
        
        # 2. Build a Max-Heap. 
        # Python's heapq is a Min-Heap by default, so we invert the counts (-cnt)
        # to force the largest counts to the top of the heap.
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n) time to arrange the heap
        
        prev = None
        res = ""
        
        # 3. Process characters as long as we have active cards or a card in "time-out"
        while maxHeap or prev:
            
            # The Impossible Check: 
            # We have a card waiting in time-out (prev), but our active hand (maxHeap) is empty.
            # There is no other unique letter left to block this duplicate letter.
            if prev and not maxHeap:
                return ""
            
            # Grab the most frequent available character from our active hand
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 # Reduce the remaining frequency (adding 1 because counts are negative)
            
            # If a card was sitting in time-out from the PREVIOUS round,
            # it is now safe to put back into our active hand (maxHeap).
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None # Clear the time-out slot
            
            # If the card we just played still has copies left, 
            # put it into the time-out slot (prev) so it rests for the next round.
            if cnt != 0:
                prev = [cnt, char]
                
        return res