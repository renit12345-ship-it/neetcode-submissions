class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=[0,0,0]
        for i in nums:
            counter[i]+=1
        r,w,b=counter
        nums[0:r]=[0]*r
        nums[r:r+w]=[1]*w
        nums[r+w:]=[2]*b
        return nums

        
        