class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the minimum possible maximum difference
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(d - mid, 0) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce all differences to at most limit
        remaining = k
        for i, d in enumerate(diff):
            remaining -= max(d - limit, 0)
            diff[i] = min(d, limit)

        # Use leftover operations to reduce some limit values by 1
        for i in range(len(diff)):
            if remaining == 0:
                break

            if diff[i] == limit:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)