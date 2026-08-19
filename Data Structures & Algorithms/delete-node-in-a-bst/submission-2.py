class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left 
            elif not root.left:
                return root.right
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val   
                root.right = self.deleteNode(root.right,curr.val)

        return root