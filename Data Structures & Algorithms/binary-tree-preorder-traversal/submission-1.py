class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        res =[]
        stack = [root] if root else []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res