class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res1=[]
        i = 0
        for i in range(min(len(word1),len(word2))) :
            res1.append(word1[i])
            res1.append(word2[i])
        res1.append(word1[i+1:])
        res1.append(word2[i+1:])

        return '' .join(res1)