class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        queue = deque()
        if "0000" in visit:
            return -1
        queue.append(["0000",0])
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        while queue:
            lock,turn = queue.popleft()
            if lock == target:
                return turn

            for child in children(lock):
                if child not in visit:
                    visit.add((child))
                    queue.append([child,turn+1])
        return -1