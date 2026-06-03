class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for row in board:
            row_set = set()
            for element in row:
                if element == '.':
                    continue
                if element in row_set:
                    return False
                else:
                    row_set.add(element)

        # Check columns
        for col in range(9):
            col_set = set()
            row_number = 0
            while row_number < 9:
                if board[row_number][col] == '.':
                    row_number += 1
                    continue
                
                if board[row_number][col] in col_set:
                    return False
                else:
                    col_set.add(board[row_number][col])

                row_number += 1
        
        # Check boxes
        box_dict = {}   
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if (row//3, col//3) in box_dict:
                    if board[row][col] in box_dict[(row//3, col//3)]:
                        return False
                    else:
                        box_dict[(row//3, col//3)].add(board[row][col])
                else:
                    box_dict[(row//3, col//3)] = {board[row][col]}

        return True