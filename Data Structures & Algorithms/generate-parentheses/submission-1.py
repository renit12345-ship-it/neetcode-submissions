class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o,c,curr):
            if o == c == 0:
                res.append(curr)
                return 
            if o > 0:
                backtrack(o-1,c,curr+"(")
            if c > o:
                backtrack(o,c-1,curr+")")
        backtrack(n,n,"")
        return res
