class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        prefix = 0
        best = [float("inf")] * n

        ans = float("inf")
        left = 0

        for right in range(n):
            prefix += arr[right]

            while prefix > target:
                prefix -= arr[left]
                left += 1

            if prefix == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != float("inf"):
                    ans = min(ans, length + best[left - 1])

                best[right] = length

            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return -1 if ans == float("inf") else ans