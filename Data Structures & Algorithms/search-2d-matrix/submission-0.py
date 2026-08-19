class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row,Col=len(matrix),len(matrix[0])
        top,bt=0,Row-1
        while top <= bt :
            row=(top+bt)//2
            if matrix[row][-1] < target :
                top= row+1
            elif matrix[row][0] > target :
                bt=row-1
            else :
                break
        if not (top <= bt):
            return False
        row= (top+bt) // 2
        l,r=0,Col-1
        while l <= r :
            m=(l+r)//2
            if matrix[row][m] < target :
                l= m+1
            elif target < matrix[row][m]:
                r=m-1
            else:
                return True 
        return False