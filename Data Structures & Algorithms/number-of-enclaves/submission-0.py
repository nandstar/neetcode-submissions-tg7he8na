class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * COLS for _ in range(ROWS)]
        q = deque()

        land, borderLand = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] == 1 and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])
                ):
                    q.append((r, c))
                    visit[r][c] = True

        while q:
            r, c = q.popleft()
            borderLand += 1
            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    grid[nr][nc] == 1 and not visit[nr][nc]
                ):
                    q.append((nr, nc))
                    visit[nr][nc] = True

        return land - borderLand
        