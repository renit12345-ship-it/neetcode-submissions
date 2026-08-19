class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums) -1 
        result = -1
        while l <=r :
            mid = (l+r)//2
            if nums[mid] < target :
                result= max(result,mid)
                l = mid+1
            elif nums[mid] >= target :
                if nums[mid] == target: return mid
                r = mid-1
        return result+1