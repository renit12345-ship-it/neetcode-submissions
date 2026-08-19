class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dim = 0
        def dfs(root) -> int:
            match root:
                case None:
                    return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right
            self.max_dim = max(self.max_dim, diameter)
            return 1 + max(left, right)
        dfs(root)
        return self.max_dim