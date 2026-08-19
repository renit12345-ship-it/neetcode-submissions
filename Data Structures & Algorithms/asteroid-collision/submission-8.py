class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        diff=0
        s1=[]
        for a in asteroids :
            while s1 and s1[-1] > 0 and a < 0 :
                diff = a+ s1[-1]
                if diff < 0 :
                    s1.pop()
                elif diff > 0 :
                    a=0
                else :
                    a=0
                    s1.pop()
            if a :
                s1.append(a)     
        return s1                  



        