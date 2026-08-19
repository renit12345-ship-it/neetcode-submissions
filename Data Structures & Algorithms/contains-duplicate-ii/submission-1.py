class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset={}
        for idx,num in enumerate(nums):
            if num in hashset and idx - hashset[num] <= k:
                return True
            hashset[num]=idx
        return False