class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res,sub = [],[]
        def backtrack():
            if len(nums) == len(sub):
                res.append(sub.copy())
                return 
            for x in count:
                if count[x] > 0:
                    sub.append(x)
                    count[x]-=1
                    backtrack()
                    count[x]+=1
                    sub.pop()
        backtrack()
        return res
                    
