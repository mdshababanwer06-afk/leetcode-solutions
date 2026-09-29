class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] = possible balances at column j
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_balances = set()

                if i == 0 and j == 0:
                    balance = 1 if grid[i][j] == '(' else -1
                    if balance >= 0:
                        dp[j].add(balance)
                    continue

                change = 1 if grid[i][j] == '(' else -1

                # From top
                if i > 0:
                    for balance in dp[j]:
                        new_balance = balance + change
                        if new_balance >= 0:
                            new_balances.add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[j - 1]:
                        new_balance = balance + change
                        if new_balance >= 0:
                            new_balances.add(new_balance)

                dp[j] = new_balances

        return 0 in dp[n - 1]