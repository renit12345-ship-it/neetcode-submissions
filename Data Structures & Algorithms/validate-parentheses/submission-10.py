class Solution:
    def isValid(self, s: str) -> bool:
        ops = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in s :
            if i in ops :
                stack.append(i)
            else :
                if not stack or ops[stack.pop()] != i:
                    return False 
        return True if len(stack) == 0 else False