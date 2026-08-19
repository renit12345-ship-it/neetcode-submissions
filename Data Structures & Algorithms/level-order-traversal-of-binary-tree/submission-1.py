# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        final = []
        while len(queue):
            res = []
            for _ in range(len(queue)):
                p = queue.popleft()
                res.append(p.val)
                if left := p.left:
                    queue.append(left)
                if right:= p.right:
                    queue.append(right)
            final.append(res)
        return final
                


