class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0

        for i in range(1, n):
            if s[i] == ')':
                # Case 1: "()"
                if s[i - 1] == '(':
                    dp[i] = 2

                    if i >= 2:
                        dp[i] += dp[i - 2]

                # Case 2: "(...)"
                else:
                    j = i - dp[i - 1] - 1

                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2

                        if j >= 1:
                            dp[i] += dp[j - 1]

                ans = max(ans, dp[i])

        return ans