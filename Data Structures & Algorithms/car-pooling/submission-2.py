class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tp = [0]*1001
        for t in trips:
            np,start,end = t
            tp[start]+=np
            tp[end]-=np
        r = 0
        for i in range(1001):
            r+=tp[i]
            if r > capacity:
                return False 
        return True
