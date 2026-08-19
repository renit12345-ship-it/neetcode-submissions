class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stacks=[]
        for right in asteroids:
            while stacks and right < 0 < stacks[-1]:
                if stacks[-1] < -right:
                    stacks.pop()
                    continue
                elif stacks[-1] == -right:
                    stacks.pop()
                break
            else:
                stacks.append(right)
        return stacks