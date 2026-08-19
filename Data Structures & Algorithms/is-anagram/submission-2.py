class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def anagram(s):
            s1=defaultdict(int)
            for i in s :
                if i in s1 :
                    s1[i]+=1
                else :
                    s1[i]=1
            return s1
        res1=anagram(s)
        res2=anagram(t)
        if res1 == res2 :
            return True
        else :
            return False