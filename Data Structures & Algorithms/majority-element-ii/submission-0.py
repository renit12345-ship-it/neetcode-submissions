class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dicts=defaultdict(int)
        results=list()
        for i in nums:
            dicts[i]+=1
        threshold=len(nums)//3
        for key,value in  dicts.items():
            if value > threshold:
                results.append(key)
        return results
        