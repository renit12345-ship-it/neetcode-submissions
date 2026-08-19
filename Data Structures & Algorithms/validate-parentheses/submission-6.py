class Solution:
    def isValid(self, s: str) -> bool:
        stacks=[]
        pairs={'(': ')', '{': '}', '[' : ']'}
        for right in s :
            if right in pairs:
                stacks.append(right)
            else :
                if not stacks or pairs[stacks.pop()] != right:
                    return False
        return not stacks