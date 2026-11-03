class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxi = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])

            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(s[right])

            maxi = max(maxi,right - left+1)

        return maxi