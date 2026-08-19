class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=[]
        lens=min(len(word1),len(word2))
        for i in range(lens):
            new.append(word1[i])
            new.append(word2[i])
        new.append(word1[lens:])
        new.append(word2[lens:])
        return ''.join(new)