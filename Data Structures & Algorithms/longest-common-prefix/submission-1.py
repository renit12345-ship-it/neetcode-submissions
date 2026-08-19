class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word=min(strs, key=len)
        longest=""
        for j in range(len(min_word)):
            for i in range(len(strs)):
                if strs[i][j] != min_word[j]:
                    return longest
            longest += min_word[j]
        return longest