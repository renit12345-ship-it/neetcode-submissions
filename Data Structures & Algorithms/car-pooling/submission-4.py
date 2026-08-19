class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
     
        total = [0]*1001
        for t in trips:
            np,s,e = t 
            total[s]+= np
            total[e]-=np
        r = 0
        for i in range(1001):
            r+=total[i]
            if r > capacity:
                return False
        return True
        