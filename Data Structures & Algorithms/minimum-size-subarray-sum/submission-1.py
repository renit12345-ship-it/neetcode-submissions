class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,CurrSum = 0,0
        res = float('Inf')
        for right in range(len(nums)) :
            CurrSum+=nums[right]
            while CurrSum >= target :
                diff = (right - left) + 1
                res = min(res,diff)
                CurrSum-=nums[left]
                left+=1
        return res if res!= float('Inf') else 0

        