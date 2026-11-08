class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        m = len(g)
        n = len(s)
        s.sort()
        g.sort()
        left = 0
        right = 0
        count = 0
        while left < m and right < n:
            if g[left] <= s[right]:
                count += 1
                left += 1
            right += 1
        return count