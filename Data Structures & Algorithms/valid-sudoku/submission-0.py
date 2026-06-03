class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_dict = {}
        col_dict = {}
        square_dict = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                    
                if r not in row_dict:
                    row_dict[r] = set()
                if c not in col_dict:
                    col_dict[c] = set()
                if (r//3, c//3) not in square_dict:
                    square_dict[(r//3, c//3)] = set()

                if (board[r][c] in row_dict[r] or board[r][c] in col_dict[c] or board[r][c] in square_dict[(r//3, c//3)]):
                    return False
                else:
                    row_dict[r].add(board[r][c])
                    col_dict[c].add(board[r][c])
                    square_dict[(r//3, c//3)].add(board[r][c])

        
        return True
