class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c=len(matrix),len(matrix[0])
        self.sum_matrix=[[0]*(c+1) for r in range(r+1)]
        for row in range(r) :
            prefix=0
            for col in range(c):
                prefix+=matrix[row][col]
                above=self.sum_matrix[row][col+1]
                self.sum_matrix[row+1][col+1]=prefix+above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2=row1+1,row2+1,col1+1,col2+1
        topleft = self.sum_matrix[row1-1][col1-1]
        top = self.sum_matrix[row1-1][col2]
        left = self.sum_matrix[row2][col1-1]
        bottom_right = self.sum_matrix[row2][col2]
        return bottom_right-top-left+topleft
