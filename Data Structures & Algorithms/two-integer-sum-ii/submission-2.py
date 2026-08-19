class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n-1

        while i < j:
            f = numbers[i]
            b = numbers[j]

            if (f+b < target):
                i+=1
            elif (f+b > target):
                j-=1
            elif (f+b == target):
                return [i+1,j+1]
        
        return [i+1,j+1]