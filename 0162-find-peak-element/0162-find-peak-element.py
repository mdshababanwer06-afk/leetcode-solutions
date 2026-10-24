class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        peak = nums[0]
        peak_index = 0

        for i in range(1, len(nums)):
            if nums[i] > peak:
                peak = nums[i]
                peak_index = i

        return peak_index