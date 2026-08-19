class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while l <= r :
            mid=(l+r)//2
            res = guess(mid)
            if res == 0 :
                return mid
            if res == 1 :
                l=mid+1
            else:
                r=mid
        return l