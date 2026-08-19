class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=[set()for _ in range(9)]
        col_set=[set() for _ in range(9)]
        col_square=[set()for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val=board[row][col]
                if val==".":
                    continue
                box_idx = (row // 3) * 3 + (col // 3)
                if val in row_set[row] or val in col_set[col] or val in col_square[box_idx]:
                    return False
                row_set[row].add(val)
                col_set[col].add(val)
                col_square[box_idx].add(val)
        return True