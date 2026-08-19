class Solution:
    def minNode(self,root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None 
        match root:
            case (TreeNode(val=pivot, left = left)) if pivot > key:
                root.left = self.deleteNode(left, key)
            case (TreeNode(val=pivot, right = right)) if pivot < key:
                root.right = self.deleteNode(right, key)
            case (TreeNode(val=pivot)):
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    min_node = self.minNode(root.right)
                    root.val = min_node.val
                    root.right = self.deleteNode(root.right, root.val)
        return root