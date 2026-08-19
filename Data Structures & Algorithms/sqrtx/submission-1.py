class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x+1
        while l < r :
            mid=(l+r)//2
            if mid*mid <= x :
                l= mid+1
            else :
                r=mid
        return l - 1