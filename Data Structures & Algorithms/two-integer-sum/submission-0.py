class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dics={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in dics:
                return [dics[diff],i]
            dics[n]=i
        return 