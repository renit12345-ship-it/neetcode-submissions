class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        lists=['+', '-', '*', '/']
        for right in tokens:
            if right == '+':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)+int(b))
            elif(right=='-'):
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)-int(b))
            elif(right=='*'):
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a)*int(b))
            elif(right=='/'):
                b=stack.pop()
                a=stack.pop()
                stack.append(int(int(a)/int(b)))
            else :
                stack.append(int(right))
        return stack[0]