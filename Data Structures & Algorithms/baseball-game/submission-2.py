class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['+','D','C']
        stack = []
        res = 0
        for i in operations :
            if i not in ops :
                stack.append(int(i))
            elif i == "+" :
                a = stack[-1]
                b= stack[-2]
                res = int(a)+int(b)
                stack.append(res)
            elif i == 'C' :
                stack.pop()
            elif i == 'D' : 
                a = stack[-1]
                res = int(a)*2
                stack.append(res)
        sums = sum(stack)
        return sums
