class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = sum(1 for x in nums if x < target)
        equal = nums.count(target)

        return list(range(smaller, smaller + equal))