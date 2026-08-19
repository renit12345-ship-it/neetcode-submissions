class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            counts=[0]*26
            for s in i :
                counts[ord(s)-ord('a')]+=1
            res[tuple(counts)].append(i)
        return list(res.values())