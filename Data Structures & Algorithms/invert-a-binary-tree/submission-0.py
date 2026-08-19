class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        if not root: return None
        while len(queue):
            len_queue = len(queue)
            for i in range(len_queue):
                curr = queue.popleft()
                curr.left, curr.right = curr.right, curr.left 
                if left:= curr.left:
                    queue.append(left)
                if right:= curr.right:
                    queue.append(right)
                    
        return root