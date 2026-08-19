class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res = r
        while l <= r :
            cap=(l+r)//2
            def hasCap(cap) :
                ship,currcap=1,cap
                for w in weights :
                    if currcap - w < 0 :
                        ship+=1
                        currcap=cap
                    currcap -=w
                return ship <= days
            if hasCap(cap) :
                res= min(res,cap)
                r= cap - 1
            else :
                l= cap + 1
        return res  


        