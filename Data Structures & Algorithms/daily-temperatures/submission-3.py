class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prefix_index = {i:num for i,num in enumerate(temperatures) }
        res = [0]*len(temperatures)
        stack=[]
        for i , n in enumerate(temperatures) :

            while stack and stack[-1][1] < n :

                stackI,stackT = stack.pop()
                res[stackI] = i - stackI


            stack.append((i,n))
        return res