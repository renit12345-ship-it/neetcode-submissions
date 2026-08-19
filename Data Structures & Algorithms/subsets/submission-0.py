class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(depth):
            if depth >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[depth])
            dfs(depth+1)
            subset.pop()
            dfs(depth+1)
        dfs(0)
        return res