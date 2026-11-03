class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_no = max(nums)
        ans = 0
        for num in nums:
            ans += max_no - num

        return ans