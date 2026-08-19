class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len,s2_len = len(s1) , len(s2)
        s1_set,s2_set = [0] * 26 , [0] * 26

        if s1_len > s2_len : return False

        for i in range(s1_len) :
            s1_set[ord(s1[i]) - ord('a')] +=1
            s2_set[ord(s2[i]) - ord('a')] +=1 
        
        if s1_set == s2_set : return True 

        for i in range(s1_len,s2_len) :
            s2_set[ord(s2[i]) - ord('a')] +=1
            s2_set[ord(s2[i-s1_len]) - ord('a')] -=1
            if s1_set == s2_set : return True 
        return False