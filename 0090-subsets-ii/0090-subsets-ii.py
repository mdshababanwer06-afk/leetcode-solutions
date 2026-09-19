class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        current = []

        def backtrack(start):
            result.append(current.copy())

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)

        return result