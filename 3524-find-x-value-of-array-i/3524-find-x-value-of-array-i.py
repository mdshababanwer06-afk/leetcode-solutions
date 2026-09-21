class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only num
            rem = num % k
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r]:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            dp = new_dp

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += dp[r]

        return result