class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts=defaultdict(int)
        for i,val in enumerate(nums):
            diff=target-val
            if diff in dicts :
                return [dicts[diff],i]
            else :
                dicts[val]=i

        