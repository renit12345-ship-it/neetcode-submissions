class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol,res = [],[]
        def backtrack():
            if len(nums) == len(sol):
                res.append(sol.copy())
                return 
            for x in nums:
                if x not in sol:
                    sol.append(x)   
                    backtrack()
                    sol.pop()
        backtrack()
        return res

            
        