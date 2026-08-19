class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        l, r = 0, len(nums) - 1  # 1. Initialize boundaries here
        
        while l <= r:
            pivot = nums[r]      # 2. Pick pivot inside the loop
            p = l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    
            # 3. Swap the pivot element in the actual array
            nums[p], nums[r] = nums[r], nums[p] 
            
            # 4. Binary search-like narrowing
            if p > k:
                r = p - 1
            elif p < k:
                l = p + 1
            else:
                return nums[p]