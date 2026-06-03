class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        COLS = len(heights[0])
        ROWS = len(heights)


        res = []
        
        def dfs(r, c, p_or_a, prevHeight):
            
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c)
             in p_or_a or heights[r][c] < prevHeight):
                return
            
            p_or_a.add((r, c))

            dfs(r + 1, c, p_or_a, heights[r][c])
            dfs(r - 1, c, p_or_a, heights[r][c])
            dfs(r, c + 1, p_or_a, heights[r][c])
            dfs(r, c - 1, p_or_a, heights[r][c])

            

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

            




