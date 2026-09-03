class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)

        # All even
        if min_odd == float('inf'):
            return True

        # Try to make everything odd
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True