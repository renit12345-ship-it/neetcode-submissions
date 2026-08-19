class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            dicts[i]=dicts.get(i,0)+1
        return max(dicts,key=dicts.get)

        