class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for dr, dc in directions:
                dfs(dr, dc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs((ROWS - 1), c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, (COLS - 1), atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
        