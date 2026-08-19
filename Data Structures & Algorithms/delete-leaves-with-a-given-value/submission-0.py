# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if not root:
                return None 
            if not (root.left and root.right) and target == root.val : return None
            root.left = self.removeLeafNodes(root.left,target)
            root.right = self.removeLeafNodes(root.right,target)
            return root

        