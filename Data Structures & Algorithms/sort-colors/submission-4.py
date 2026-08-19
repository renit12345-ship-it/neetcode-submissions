class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_red=0
        count_blue=0
        count_white=0
        for i in nums:
            if i == 1:
                count_white += 1
            elif i == 0 :
                count_red += 1
            else :
                count_blue += 1
        nums[:count_red] = [0]*count_red
        nums[count_red:count_red+count_white]=[1]*count_white
        nums[count_red+count_white:] = [2]*count_blue