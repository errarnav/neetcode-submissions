class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0
        area = 0
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0

        def bfs(r, c, a):

            q = collections.deque()
            grid[r][c] = 0
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                visited.add((r, c))
                a += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS
                        or (nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    else:
                        q.append((nr, nc))
                        grid[nr][nc] = 0


            return a



        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = bfs(row, col, 0)
                    maxArea = max(curr_area, maxArea)

        
        return maxArea


