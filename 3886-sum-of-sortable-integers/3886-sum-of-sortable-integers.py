class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        # Prefix maximum
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Suffix minimum
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Prefix count of adjacent descents
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = (
                pref_drop[i - 1] + (nums[i - 1] > nums[i])
            )

        def check(k: int) -> bool:
            for start in range(0, n, k):
                end = start + k - 1

                # Count descents, including the circular boundary
                drops = pref_drop[end] - pref_drop[start]
                if nums[end] > nums[start]:
                    drops += 1

                # Each block must be circularly non-decreasing
                if drops > 1:
                    return False

                # Values in earlier blocks must not exceed
                # values in later blocks
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        ans = 0

        # Enumerate divisors of n
        d = 1
        while d * d <= n:
            if n % d == 0:
                if check(d):
                    ans += d

                other = n // d
                if other != d and check(other):
                    ans += other

            d += 1

        return ans
