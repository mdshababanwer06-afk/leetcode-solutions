class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Cannot sort a reversed string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum is already first, or maximum is already last
        if s[0] == mn or s[-1] == mx:
            return 1

        # Minimum or maximum occurs in the middle
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Minimum is last and maximum is first
        return 3