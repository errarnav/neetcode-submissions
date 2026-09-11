class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        ROWS, COLS, land = len(grid), len(grid[0]), 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        distance = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            qLen = len(q)

            for _ in range(qLen):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == land):
                        grid[nr][nc] = distance
                        q.append((nr, nc))
                
            distance += 1
        