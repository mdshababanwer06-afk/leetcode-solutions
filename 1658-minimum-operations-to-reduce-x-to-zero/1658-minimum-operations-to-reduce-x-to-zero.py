class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)

        total = sum(nums)
        target = total - x

        if target == 0:
            return n

        if target < 0:
            return -1

        left = 0
        curr_sum = 0
        max_length = -1

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == -1:
            return -1

        return n - max_length