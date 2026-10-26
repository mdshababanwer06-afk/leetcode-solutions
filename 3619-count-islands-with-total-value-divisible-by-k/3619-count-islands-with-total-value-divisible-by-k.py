class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0

            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)

            return val

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    total = dfs(r, c)

                    if total % k == 0:
                        count += 1

        return count