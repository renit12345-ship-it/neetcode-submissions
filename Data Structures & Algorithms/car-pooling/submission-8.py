class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        totaltrips = [0] * 1001
        for np,start,end in trips:
            totaltrips[start]+= np
            totaltrips[end]-= np    
        cur = 0
        for change in totaltrips:
            cur+= change
            if cur > capacity:
                return False
        return True

        