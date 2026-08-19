class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Standard Mountain Logic:
        # We use len(nums) because the insert position can be 
        # at the very end of the list.
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                # Target is definitely to the right of mid
                left = mid + 1
            else:
                # nums[mid] >= target
                # This mid could be the answer, so we don't skip it
                right = mid
        
        # When left == right, we've found the insertion point
        return left