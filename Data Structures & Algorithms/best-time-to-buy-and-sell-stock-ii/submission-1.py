class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for curr in range(1,len(prices)) :
            if prices[curr] > prices[curr -1] :
                profit+=prices[curr]-prices[curr-1]
        return profit


        