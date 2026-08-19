class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,currSum):
            if not root:
                return False 
            currSum += root.val
            if not root.left and not root.right:
                return currSum == targetSum
            return dfs(root.left,currSum) or dfs(root.right,currSum)
        return dfs(root,0)