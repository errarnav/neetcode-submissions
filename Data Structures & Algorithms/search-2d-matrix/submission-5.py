class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find which row the tarrget should be in (if it exists)
        ROWS, COLS = len(matrix), len(matrix[0])
        
        l, r = 0, ROWS - 1

        while l <= r:
            row = l + (r - l)//2

            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                break
        if l <= r:
            row = l + (r - l)//2
        else:
            return False
        
        l, r = 0, COLS - 1

        
        while l <= r:
            m = l + (r - l)//2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        
        return False
