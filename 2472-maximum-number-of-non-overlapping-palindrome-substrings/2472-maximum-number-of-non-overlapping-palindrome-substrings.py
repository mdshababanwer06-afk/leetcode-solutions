class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Precompute palindromes
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (
                    length <= 2 or pal[i + 1][j - 1]
                ):
                    pal[i][j] = True

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Skip current character
            dp[i] = dp[i - 1]

            # Take a palindrome ending at i - 1
            for j in range(i - k + 1):
                if pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]