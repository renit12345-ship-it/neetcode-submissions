class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        k = len(nums)-k
        while l<=r:
            p,pivot = l, nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]
            if k < p:
                r= p-1
            elif p < k:
                l = p+1
            else:
                return nums[p]

        