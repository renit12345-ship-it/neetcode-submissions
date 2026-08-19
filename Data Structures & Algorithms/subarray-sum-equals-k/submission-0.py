class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum=0
        count=0
        dics={0:1}
        for i in range(len(nums)):
            current_sum+=nums[i]
            diff=current_sum-k
            if diff in dics:
                count+=dics[diff]
            dics[current_sum]=dics.get(current_sum,0)+1
        return count
        