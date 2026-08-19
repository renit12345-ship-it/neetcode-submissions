class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=min(strs,key=len)
        for i in range(len(shortest)):
            char=shortest[i]
            for other_words in strs:
                if other_words[i]!=char:
                    return shortest[:i]
        return shortest
        