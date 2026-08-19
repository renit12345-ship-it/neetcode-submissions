class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        l,r = 0, len(nums)-1
        while l<=r :
            p,pivot = l,nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i],nums[p] = nums[p],nums[i]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]
            if p > k:
                r= p-1
            elif p < k:
                l= p+1
            else:
                return nums[p]

            
