class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        pmax=0
        while r < len(prices) :
            if prices[l]<prices[r]:
                pmax=max(pmax, prices[r]-prices[l])
            else:
                l=r
            r+=1
                
        return pmax