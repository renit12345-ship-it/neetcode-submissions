# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while len(queue):
            level_length = len(queue)
            for i in range(len(queue)):
                p = queue.popleft()
                if i == level_length-1:
                    res.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        return res
                
        