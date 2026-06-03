class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row = [False] * ROWS
        col = [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if row[r] or col[c] == True:
                    matrix[r][c] = 0