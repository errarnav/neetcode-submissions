class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        safe = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):

            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in safe or board[r][c] == 'X':
                return

            safe.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe:
                    board[r][c] = 'X'
        
