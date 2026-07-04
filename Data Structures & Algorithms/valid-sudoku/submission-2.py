class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row_set = set()
            for elem in row:
                if elem in row_set:
                    return False
                if elem == '.':
                    continue
                else:
                    row_set.add(elem)

        
        for col in range(9):
            col_set = set()
            for row in board:
                if row[col] in col_set:
                    return False
                if row[col] == '.':
                    continue
                else:
                    col_set.add(row[col])

        squares = {}
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] in squares[(row // 3, col //3)]:
                    return False
                if board[row][col] == '.':
                    continue
                else:
                    squares[(row // 3, col //3)].add(board[row][col])

        return True


