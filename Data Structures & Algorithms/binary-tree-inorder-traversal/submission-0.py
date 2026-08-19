class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        match root:
            case None:
                return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)