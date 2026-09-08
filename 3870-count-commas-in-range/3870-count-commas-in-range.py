class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        if n < 1_000_000:
            return n - 999

        if n < 1_000_000_000:
            return (n - 999) + (n - 999_999)

        return (n - 999) + (n - 999_999) + (n - 999_999_999)