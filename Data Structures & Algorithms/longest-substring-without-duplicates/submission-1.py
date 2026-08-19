class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, res = 0 , 0
        for i in range(len(s)) :
            while s[i] in seen :
                seen.remove(s[left])
                left+=1
            res = max(res,(i-left)+1)
            seen.add(s[i])

        return res

            
        