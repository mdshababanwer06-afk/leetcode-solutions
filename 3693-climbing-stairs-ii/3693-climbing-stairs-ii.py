class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for step in (1, 2, 3):
                if i - step >= 0:
                    # dp to previous step + step^2 jump cost
                    dp[i] = min(dp[i], dp[i - step] + step * step)
            
            # Add step i cost (costs is 1-indexed in problem, so costs[i - 1] in Python)
            dp[i] += costs[i - 1]
            
        return dp[n]