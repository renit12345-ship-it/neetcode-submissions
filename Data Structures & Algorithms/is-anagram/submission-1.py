class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics1,dics2={},{}
        for i in s:
            dics1[i] = dics1.get(i, 0) + 1
        for j in t:
            dics2[j]=dics2.get(j,0)+1
        if dics1==dics2:
            return True
        else:
            return False
        
        