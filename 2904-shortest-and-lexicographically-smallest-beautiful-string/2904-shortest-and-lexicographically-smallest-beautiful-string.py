class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        count = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                count += 1

            if count == k:
                # Remove leading zeros
                while s[left] == '0':
                    left += 1

                cur = s[left:right + 1]

                if (not ans or
                    len(cur) < len(ans) or
                    (len(cur) == len(ans) and cur < ans)):
                    ans = cur

                # Remove the first 1
                count -= 1
                left += 1

        return ans