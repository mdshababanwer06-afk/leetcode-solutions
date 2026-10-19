class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        stored =[]
        for i in range(0,len(nums)):
            if nums[i] == target:
                stored.append(i)

        return stored