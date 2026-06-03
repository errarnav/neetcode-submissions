class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        COLS = len(matrix[0])
        ROWS = len(matrix)

        proc = {'right': COLS, 'down': ROWS, 'left': 0, 'up': 0}
        
        count = 0
        for r in matrix:
            for c in r:
                count += 1
        
        res = []
        process = 'right'
        row = 0
        col = -1

        while len(res) < count:

            if process == 'right':
                col += 1

                while col < proc['right']:
                    res.append(matrix[row][col])
                    col += 1
                
                col -= 1
                proc['right'] -= 1
                process = 'down'
                continue


            if process == 'down':
                row += 1
                while row < proc['down']:
                    res.append(matrix[row][col])
                    row += 1

                row -= 1
                proc['down'] -= 1
                process = 'left'
                continue


            if process == 'left':
                col -= 1

                while col >= proc['left']:
                    res.append(matrix[row][col])
                    col -= 1

                col += 1
                proc['left'] += 1
                process = 'up'
                continue

            if process == 'up':
                row -= 1

                while row > proc['up']:
                    res.append(matrix[row][col])
                    row -= 1

                row += 1
                proc['up'] += 1
                process = 'right'
                continue
        
        return res


            

                    





            