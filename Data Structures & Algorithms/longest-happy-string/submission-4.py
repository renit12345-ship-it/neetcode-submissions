class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap,res =[], ""
        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count!=0:
                heapq.heappush(heap,(count,char))
        while heap:
            cnt,char = heapq.heappop(heap)
            if len(res) > 1 and res[-1]==res[-2]== char:
                if not heap:
                    break
                cnt2,char2 = heapq.heappop(heap)
                cnt2+=1
                res+=char2
                if cnt2:
                    heapq.heappush(heap,(cnt2,char2))
            else:
                cnt+=1
                res+=char 
            if cnt:
                heapq.heappush(heap,(cnt,char))

        return res
            

                
