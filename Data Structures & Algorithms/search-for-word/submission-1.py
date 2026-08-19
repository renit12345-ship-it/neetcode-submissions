class Solution:
    def dfs(self,board,word,row,col,ind):

        if ind >= len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col]!= word[ind]:
            return False 
        temp = board[row][col]
        board[row][col] = ""
        found = self.dfs(board,word,row-1,col,ind+1) or self.dfs(board,word,row+1,col,ind+1) or self.dfs(board,word,row,col-1,ind+1) or self.dfs(board,word,row,col+1,ind+1)
        board[row][col] = temp
        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and self.dfs(board,word,r,c,0):
                    return True
        return False
        