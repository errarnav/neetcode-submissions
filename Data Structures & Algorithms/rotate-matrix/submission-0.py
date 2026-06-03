class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)

        for row in range(ROWS // 2):
            for col in range(ROWS):
                curr = matrix[row][col]
                new = matrix[ROWS - row - 1][col]

                matrix[row][col] = new
                matrix[ROWS - row - 1][col] = curr

        col = 0
        row = 0
        while row < ROWS and col < ROWS:
                if row == col:
                    col = 0
                    row += 1
                else:
                    curr = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = curr
                    col += 1

