class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)