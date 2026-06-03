class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        while l <= r:

            m = l + ((r - l) // 2)

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                l = m + 1
            else:
                return True
            
        
        row = r


        full_row = matrix[row]
        l = 0
        r = len(full_row) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target < full_row[m]:
                r = m - 1

            elif target > full_row[m]:
                l = m + 1
            
            else:
                return True

        return False
