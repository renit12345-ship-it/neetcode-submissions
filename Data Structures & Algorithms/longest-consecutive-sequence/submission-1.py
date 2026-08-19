class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        set_nums=set(nums)
        for num in set_nums : 
            if num-1 not in set_nums:
                current=1 
                while num+current in set_nums :
                    current+=1
                    
                longest=max(longest,current)
        return longest