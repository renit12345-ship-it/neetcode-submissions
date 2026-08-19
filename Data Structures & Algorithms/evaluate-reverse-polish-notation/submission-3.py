class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = [ '+', '-', '*', '/']
        stack = []

        for i in tokens :
            if i == '+' :
                a = stack.pop()
                b= stack.pop()
                stack.append(int(b)+ int(a))
            
            elif i == '-' :
                a = stack.pop()
                b= stack.pop()
                stack.append(int(b) - int(a))

            

            elif i == '*' :
                a = stack.pop()
                b= stack.pop()
                stack.append(int(b)*int(a))

            
            elif i == '/' :
                a = stack.pop()
                b= stack.pop()
                stack.append(int(int(b) / int(a)))

            else :
                stack.append(int(i))
        return stack[0]