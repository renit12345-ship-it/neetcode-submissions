class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        if not root:
            return []
        while len(queue):
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                if i == level_size-1: res.append(curr.val)
                if left:= curr.left:
                    queue.append(left)
                if right:= curr.right:
                    queue.append(right)
        return res