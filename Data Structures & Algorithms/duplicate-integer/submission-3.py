class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for value in nums:
            if value in seen:      # we've seen this number before → duplicate
                return True
            seen[value] = 1        # mark it as seen
        return False               # no duplicates found

        