class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = 0
        max_index = 0

        for i in range(n):
            if nums[i] < nums[min_index]:
                min_index = i

            if nums[i] > nums[max_index]:
                max_index = i

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        front = right + 1
        back = n - left
        both = left + 1 + n - right

        return min(front, back, both)