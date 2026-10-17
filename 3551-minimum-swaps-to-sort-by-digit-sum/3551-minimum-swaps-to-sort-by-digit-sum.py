class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        arr = sorted((digit_sum(x), x, i) for i, x in enumerate(nums))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle += 1

            swaps += max(0, cycle - 1)

        return swaps