class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        empySpaceExists = False
        freshFruitExists = False

        q = collections.deque()

        
        def addCell(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return

            q.append([r, c])
            visited.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))

                if grid[r][c] == 1:
                    freshFruitExists = True
                if grid[r][c] == 0:
                    empySpaceExists = True

        
        time = -1
        
        if not q:
            if freshFruitExists:
                return -1
            else:
                return 0

        while q:
            for i in range(len(q)):

                r, c = q.popleft()
                grid[r][c] = grid[r][c] * -1

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            time += 1

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    return -1

        return time