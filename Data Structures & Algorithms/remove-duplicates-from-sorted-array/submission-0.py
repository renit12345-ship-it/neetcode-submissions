class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        s=set()
        for fast in range(len(nums)):
            if nums[fast] not in s:
                nums[slow]=nums[fast]
                slow+=1
            s.add(nums[fast])
        return slow