class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacks=[]
        for right in operations:
            if right not in ['+', 'D', 'C']:
                stacks.append(int(right))
            elif right == '+':
                a=stacks.pop()
                b=stacks.pop()
                stacks.append(b)
                stacks.append(a)
                stacks.append(a+b)
            elif right == 'D':
                stacks.append(stacks[-1] * 2)
            elif right == 'C':
                stacks.pop()
        return sum(stacks)