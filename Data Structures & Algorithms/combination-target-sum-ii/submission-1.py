class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                # FIX 3: twins must stand next to each other
        sub, res = [], []

        def dfs(i, total):
            # 🚪 Door 1: hit the target → snapshot 📸
            if total == target:
                res.append(sub.copy())
                return
            # FIX 2: "out of numbers OR overshot" → either one stops us
            if i >= len(candidates) or total > target:
                return

            # CHOICE 1: include candidates[i] — used up → move on!
            sub.append(candidates[i])
            dfs(i + 1, total + candidates[i])   # FIX 1: i+1 (one use per number)
            sub.pop()

            # CHOICE 2: skip candidates[i] — skip the WHOLE twin family
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1                      # hop over every identical copy
            dfs(i + 1, total)               # skip → total untouched

        dfs(0, 0)
        return res