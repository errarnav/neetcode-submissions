class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def bfs(r, c):

            grid[r][c] = '0'

            
            q = collections.deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r +  dr
                    nc = c + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'):
                        continue
                    else:
                        q.append((nr, nc))
                        grid[nr][nc] = '0'

            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
                else:
                    continue


        return islands