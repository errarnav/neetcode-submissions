class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # if cell below it exists, perform dfs on it

            grid[r][c] = '0'
            visited.add((r, c))
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or 
                    grid[nr][nc] == '0' or (nr, nc) in visited):
                    continue
                else:
                    dfs(nr, nc)

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        
        return islands