class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for index,val in enumerate(nums):
            complement= target-val
            if complement in dicts:
                return [dicts[complement],index]
            dicts[val]=index
        return True