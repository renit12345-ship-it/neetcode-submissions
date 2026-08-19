class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets=set()
        slow=0
        counts=0
        for fast in range(len(s)):
            while s[fast] in sets:
                sets.remove(s[slow])
                slow+=1
            sets.add(s[fast])
            counts=max(counts, fast - slow + 1)
        return counts
