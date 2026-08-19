class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dics={}
        for index,val in enumerate(nums):
            complement=target-val
            if complement in dics:
                return [dics[complement],index]
            dics[val]=index
        return True
